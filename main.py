import ebooklib
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pdfplumber
from ebooklib import epub
from bs4 import BeautifulSoup
import io
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import re

def fix_broken_words(text: str) -> str:
    # Remove hyphen + line break when a word is clearly split
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    return text


def normalize_text(text):
    text = re.sub(r'\n+', '\n', text)
    lines = text.split("\n")

    paragraphs = []
    buffer = ""

    for line in lines:
        line = line.strip()

        if not line:
            if buffer:
                paragraphs.append(buffer.strip())
                buffer = ""
            continue

        # HARD BREAK for chapter headings
        if re.match(r'^chapter\s+\d+', line, re.I):
            if buffer:
                paragraphs.append(buffer.strip())
                buffer = ""
            paragraphs.append(line)
            continue

        buffer += (" " if buffer else "") + line

        if re.search(r'[.!?]["\']?$', line):
            paragraphs.append(buffer.strip())
            buffer = ""

    if buffer:
        paragraphs.append(buffer.strip())

    return paragraphs

def normalize_quotes(text: str) -> str:
    # Normalize smart quotes to plain quotes (optional but safer)
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("‘", "'").replace("’", "'")

    # Ensure space before a quote if it follows punctuation
    text = re.sub(r'([.!?])(")', r'\1 \2', text)

    # If two quotes touch, separate them
    text = re.sub(r'"{2,}', '"\n"', text)

    return text

def split_adjacent_quotes(text: str) -> str:
    # Split ONLY when a quoted sentence is followed by another quoted sentence
    text = re.sub(
        r'([.!?])\s*["\']\s+(?=["\'])',
        r'\1"\n\n',
        text
    )
    return text


def wrap(text, max_chars=70):
    words = text.split(" ")
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) <= max_chars:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)
    return lines

def extract_epub(file_bytes):
    book = epub.read_epub(io.BytesIO(file_bytes))
    text = ""
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "html.parser")
        text += soup.get_text() + "\n\n"
    
    return text

def extract_text(file: UploadFile, file_bytes: bytes):
    name = file.filename.lower()

    if name.endswith(".epub"):
        return extract_epub(file_bytes)
    else:
        text = ""
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n\n"
        return text

def structure_text(text: str):
    paragraphs = normalize_text(text)
    blocks = []

    for para in paragraphs:
        if para.lower().startswith("chapter"):
            blocks.append({
                "type": "chapter",
                "text": para
            })
        else:
            blocks.append({
                "type": "paragraph",
                "text": para
            })

    return blocks

def format_blocks(blocks):
    pages = []
    current_page = ""

    for block in blocks:
        # New page for chapters
        if block["type"] == "chapter" and current_page:
            pages.append(current_page)
            current_page = ""

        max_chars = 60 if block["type"] == "chapter" else 75

        for line in wrap(block["text"], max_chars):
            current_page += line + "\n"

        # Paragraph spacing
        current_page += "\n" if block["type"] == "paragraph" else "\n\n"

    if current_page:
        pages.append(current_page)

    return pages



@app.post("/upload")
async def upload(file: UploadFile = File(...)): 

    file_bytes = await file.read()
    text = extract_text(file, file_bytes)
    text = fix_broken_words(text)
    text = normalize_quotes(text)
    text = split_adjacent_quotes(text)

    blocks = structure_text(text)
    pages = format_blocks(blocks)

    return {"pages": pages}

@app.post("/download", response_class=StreamingResponse)
async def download(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text(file, file_bytes)
    text = fix_broken_words(text)
    text = normalize_quotes(text)
    text = split_adjacent_quotes(text)

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    def new_page():
        c.setFillColorRGB(0,0,0)
        c.rect(0, 0, width, height, fill=1)
        c.setFillColorRGB(1,1,1)
        c.setFont("Helvetica", 14)

    new_page()
    y = height - 40

    blocks = structure_text(text)
    pages = format_blocks(blocks)

    for page_text in pages:
        c.showPage()
        new_page()
        y = height - 40

        for line in page_text.split("\n"):
            if y < 40:
                c.showPage()
                new_page()
                y = height - 40

            c.drawString(40, y, line)
            y -= 18

    c.save()
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=darkmode.pdf"}
    )

