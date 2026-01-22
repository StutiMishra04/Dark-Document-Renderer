import { useState } from "react";

function App() {
  const [pages, setPages] = useState([]);
  const [page, setPage] = useState(0);
  const [file, setFile] = useState(null);

  const upload = async (e) => {
    const selected = e.target.files[0];
    setFile(selected);

    const formData = new FormData();
    formData.append("file", selected);

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setPages(data.pages);
    setPage(0);
  };

  const download = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/download", {
      method: "POST",
      body: formData,
    });

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "darkmode.pdf";
    a.click();

    window.URL.revokeObjectURL(url);
  };

  return (
    <div
      style={{
        backgroundColor: "black",
        color: "white",
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Dark PDF Reader</h1>

      <div style={{ textAlign: "center", marginBottom: "20px" }}>
        <input type="file" onChange={upload} />
      </div>

      {pages.length > 0 && (
        <>
          <div
            style={{
              maxWidth: "700px",
              margin: "40px auto",
              background: "#111",
              padding: "40px",
              borderRadius: "10px",
              fontSize: "18px",
              lineHeight: "1.7",
              boxShadow: "0 0 30px rgba(255,255,255,0.1)",
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
              fontFamily: "'Cinzel', serif",
              letterSpacing: "0.05em",
            }}
          >
            {pages[page]}
          </div>

          <div style={{ textAlign: "center", marginBottom: "40px" }}>
            <button onClick={() => setPage((p) => p - 1)} disabled={page === 0}>
              ◀ Prev
            </button>

            <span style={{ margin: "0 20px" }}>
              Page {page + 1} / {pages.length}
            </span>

            <button
              onClick={() => setPage((p) => p + 1)}
              disabled={page === pages.length - 1}
            >
              Next ▶
            </button>

            <br />
            <br />

            <button onClick={download}>⬇ Download Dark PDF</button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
