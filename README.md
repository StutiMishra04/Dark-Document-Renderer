<h1>DarkDoc</h1>

<p>DarkDoc is a dark-mode document reader and formatter that converts PDFs, EPUBs, and raw text (such as audiobook or YouTube transcripts) into a structured, book-style reading experience.
It prioritizes readability, structure correction, and consistent formatting rather than simple file conversion.</p>

<h2>Features</h2>

<p>Upload PDF and EPUB files</p>
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

<h2>Architecture Overview</h2>
<div>- Input (PDF / EPUB / Text)</div>
<div>- Text Cleaning & Normalization</div>
<div>- Chapter & Paragraph Detection</div>
<div>- Structural Correction</div>
<div>- Pagination Engine</div>
<div>- Reader View / PDF Export</div>

<h2>Tech Stack</h2>

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

<h2>Project Structure</h2>
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

Use environment variables for configuration.

License

MIT License.
