<h1>DarkDoc</h1>

<p>DarkDoc is a dark-mode document reader and formatter that converts PDFs, EPUBs, and raw text (such as audiobook or YouTube transcripts) into a structured, book-style reading experience.
It prioritizes readability, structure correction, and consistent formatting rather than simple file conversion.</p>

<h2>Features</h2>

<link>Upload PDF and EPUB files</link>
<p>Paste raw transcripts or text</p>
<p>Automatic dark-mode formatting</p>

<p>Chapter-aware pagination</p>

<p>Fixes common extraction issues:</p>
<div>- Broken words</div>
<div>- Incorrect line breaks</div>
<div>- Dialogue collisions</div>
<div>- Quote inconsistencies</div>

Book-style page navigation
Export formatted output as a dark-mode PDF

Architecture Overview
<div>- Input (PDF / EPUB / Text)</div>
<div>- Text Cleaning & Normalization</div>
<div>- Chapter & Paragraph Detection</div>
<div>- Structural Correction</div>
<div>- Pagination Engine</div>
<div>- Reader View / PDF Export</div>

Tech Stack

<b>Backend</b>

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
<div>darkdoc/</div>
<div>│</div>
<div>├── backend/</div>
<div>│   ├── app/</div>
<div>│   │   ├── main.py</div>
<div>│   │   ├── routes/</div>
<div>│   │   ├── services/</div>
<div>│   │   ├── utils/</div>
<div>│   │   └── models/</div>
<div>│   ├── requirements.txt</div>
<div>│</div>
<div>├── frontend/</div>
<div>│   ├── src/</div>
<div>│   │   ├── components/</div>
<div>│   │   ├── pages/</div>
<div>│   │   ├── hooks/</div>
<div>│   │   └── styles/</div>
<div>│   ├── package.json</div>
<div>│</div>
<div>├── .gitignore</div>
<div>├── LICENSE</div>
<div>└── README.md</div>

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
