import PropTypes from "prop-types";
import { riskConfig } from "../utils/riskConfig";

export default function ClauseCard({ clause }) {
  const config = riskConfig[clause.risk] || riskConfig.MEDIUM;

  return (
    <article style={{ border: `1px solid ${config.color}33`, borderRadius: 18, padding: 18, background: "#fff" }}>
      <div style={{ display: "flex", justifyContent: "space-between", gap: 12, alignItems: "center" }}>
        <strong>{clause.title}</strong>
        <span style={{ color: config.color, fontWeight: 700 }}>{config.icon} {config.label}</span>
      </div>
      <p style={{ margin: "8px 0", color: "#6b7280" }}>{clause.category} · Score {clause.score}/100</p>
      <div style={{ padding: 12, background: "#f8fafc", borderRadius: 12, marginBottom: 12 }}>{clause.clauseText}</div>
      <p><strong>Why it matters:</strong> {clause.explanation}</p>
      <p><strong>Recommendation:</strong> {clause.recommendation}</p>
    </article>
  );
}

ClauseCard.propTypes = {
  clause: PropTypes.shape({
    title: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
    risk: PropTypes.string.isRequired,
    score: PropTypes.number.isRequired,
    clauseText: PropTypes.string.isRequired,
    explanation: PropTypes.string.isRequired,
    recommendation: PropTypes.string.isRequired,
  }).isRequired,
};
