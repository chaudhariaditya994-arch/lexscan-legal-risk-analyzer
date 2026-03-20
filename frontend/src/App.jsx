import { useState } from "react";
import UploadView from "./components/UploadView";
import ResultView from "./components/ResultView";
import HistoryView from "./components/HistoryView";
import { useAnalyzer } from "./hooks/useAnalyzer";
import { useMongoStore } from "./hooks/useMongoStore";

export default function App() {
  const { analyze, loading, error } = useAnalyzer();
  const { history, add, clear } = useMongoStore();
  const [result, setResult] = useState(null);

  async function handleFile(file) {
    const payload = await analyze(file);
    const enriched = {
      ...payload,
      id: crypto.randomUUID(),
    };
    setResult(enriched);
    add(enriched);
  }

  return (
    <main style={{ minHeight: "100vh", background: "linear-gradient(135deg, #eff6ff, #f8fafc)", padding: 32, fontFamily: "Inter, system-ui, sans-serif" }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", display: "grid", gap: 24 }}>
        <header>
          <p style={{ marginBottom: 8, fontWeight: 700, color: "#1d4ed8" }}>LEXSCAN</p>
          <h1 style={{ margin: 0, fontSize: 48 }}>AI Legal Risk Analyzer</h1>
          <p style={{ maxWidth: 700, color: "#475569" }}>Upload a PDF contract and get structured risk analysis, clause-level flags, plain English explanations, and a reusable history timeline.</p>
        </header>
        <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 24 }}>
          <div style={{ display: "grid", gap: 24 }}>
            <UploadView onFileSelect={handleFile} disabled={loading} />
            {loading ? <p>Analyzing contract with Claude...</p> : null}
            {error ? <p style={{ color: "#dc2626" }}>{error}</p> : null}
            {result ? <ResultView result={result} /> : null}
          </div>
          <HistoryView history={history} onSelect={setResult} onClear={clear} />
        </div>
      </div>
    </main>
  );
}
