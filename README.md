DarkDoc 

DarkDoc is a dark-mode document reader and formatter that converts PDFs, EPUBs, and pasted text (such as audiobook or YouTube transcripts) into a clean, book-style reading experience.
It focuses on readability and structure, not just file conversion.

Features

1 -> Upload PDF and EPUB files
2 -> Paste raw text / transcripts
3 -> Automatic dark-mode formatting
4 -> Chapter-aware pagination
5 -> Fixes common extraction issues:
  Broken words
  Bad line breaks
  Dialogue collisions
  Quote inconsistencies

6 -> Book-style page navigation
7 -> Download as a dark-mode PDF

Tech Stack
1 -> Backend: FastAPI (Python)
2 -> Frontend: React
3 -> PDF Extraction: pdfplumber
4 -> EPUB Parsing: ebooklib + BeautifulSoup
5 -> PDF Generation: ReportLab

All input types follow the same pipeline:

Input (PDF / EPUB / Text)
→ Clean & normalize text
→ Detect chapters & paragraphs
→ Format into logical pages
→ Display in reader / export PDF

This ensures consistent formatting across all sources.
