import PropTypes from "prop-types";

export default function HistoryView({ history, onSelect, onClear }) {
  return (
    <section style={{ background: "#fff", borderRadius: 24, padding: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h3 style={{ marginTop: 0 }}>Session history</h3>
        <button type="button" onClick={onClear}>Clear</button>
      </div>
      {history.length === 0 ? <p>No analysis sessions yet.</p> : null}
      <div style={{ display: "grid", gap: 10 }}>
        {history.map((entry) => (
          <button
            key={entry.id}
            type="button"
            onClick={() => onSelect(entry)}
            style={{ padding: 14, borderRadius: 16, border: "1px solid #cbd5e1", textAlign: "left", background: "#f8fafc" }}
          >
            <strong>{entry.documentTitle}</strong>
            <div style={{ color: "#475569" }}>{entry.overallRisk} · {entry.overallRiskScore}/100</div>
          </button>
        ))}
      </div>
    </section>
  );
}

HistoryView.propTypes = {
  history: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.string.isRequired,
    documentTitle: PropTypes.string.isRequired,
    overallRisk: PropTypes.string.isRequired,
    overallRiskScore: PropTypes.number.isRequired,
  })).isRequired,
  onSelect: PropTypes.func.isRequired,
  onClear: PropTypes.func.isRequired,
};
