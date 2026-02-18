DarkDoc

DarkDoc is a dark-mode document reader and formatter that converts PDFs, EPUBs, and raw text (such as audiobook or YouTube transcripts) into a structured, book-style reading experience.
It prioritizes readability, structure correction, and consistent formatting rather than simple file conversion.

Features

Upload PDF and EPUB files
Paste raw transcripts or text
Automatic dark-mode formatting

Chapter-aware pagination

Fixes common extraction issues:
Broken words
Incorrect line breaks
Dialogue collisions
Quote inconsistencies

Book-style page navigation
Export formatted output as a dark-mode PDF

Architecture Overview
<div>-> Input (PDF / EPUB / Text)</div>
        ↓
<div>-> Text Cleaning & Normalization</div>
        ↓
<div>-> Chapter & Paragraph Detection</div>
        ↓
<div>-> Structural Correction</div>
        ↓
<div>-> Pagination Engine</div>
        ↓
<div>-> Reader View / PDF Export</div>

Tech Stack

Backend

FastAPI (Python)

Frontend

React

PDF Extraction

pdfplumber

EPUB Parsing

ebooklib

BeautifulSoup

PDF Generation

ReportLab

Project Structure
darkdoc/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── models/
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── styles/
│   ├── package.json
│
├── .gitignore
├── LICENSE
└── README.md

Installation
Clone the repository
git clone https://github.com/your-username/darkdoc.git
cd darkdoc

Backend setup
cd backend
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs at:
http://127.0.0.1:8000

Frontend setup
cd frontend
npm install
npm start


Frontend runs at:
http://localhost:3000

API Endpoints
Method	Endpoint	Description
POST	/upload/pdf	Upload PDF file
POST	/upload/epub	Upload EPUB file
POST	/upload/text	Submit raw text
GET	/export/pdf	Download formatted PDF
Development Notes

Enable CORS in FastAPI for frontend integration.

Keep formatting logic modular inside services/.

Use environment variables for configuration.

License

MIT License.
