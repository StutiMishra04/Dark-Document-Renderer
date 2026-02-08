DarkDoc

DarkDoc is a dark-mode document reader and formatter that converts PDFs, EPUBs, and pasted text (such as audiobook or YouTube transcripts) into a clean, book-style reading experience.

It focuses on readability and structure, not just file conversion.

✨ Features:

📄 Upload PDF and EPUB files

✍️ Paste raw text / transcripts

🌙 Automatic dark-mode formatting

📚 Chapter-aware pagination

🧠 Fixes common extraction issues:

Broken words

Bad line breaks

Dialogue collisions

Quote inconsistencies

📖 Book-style page navigation

⬇️ Download as a dark-mode PDF

🏗️ Tech Stack

Backend: FastAPI (Python)

Frontend: React

PDF Extraction: pdfplumber

EPUB Parsing: ebooklib + BeautifulSoup

PDF Generation: ReportLab

🔄 Processing Pipeline

All input types follow the same formatting pipeline:

Input (PDF / EPUB / Text)
→ Clean & normalize text
→ Detect chapters & paragraphs
→ Format into logical pages
→ Display in reader / export PDF


This ensures consistent formatting across all sources.
