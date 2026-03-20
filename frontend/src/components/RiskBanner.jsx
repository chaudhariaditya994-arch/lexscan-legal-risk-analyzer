import PropTypes from "prop-types";
import { riskConfig } from "../utils/riskConfig";

export default function RiskBanner({ overallRisk, overallRiskScore, executiveSummary, negotiationSummary, cached }) {
  const config = riskConfig[overallRisk] || riskConfig.MEDIUM;

  return (
    <section style={{ background: "#fff", borderRadius: 24, padding: 24, border: `1px solid ${config.color}33` }}>
      <div style={{ display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 16 }}>
        <div>
          <p style={{ margin: 0, color: config.color, fontWeight: 800 }}>{config.label}</p>
          <h2 style={{ margin: "6px 0 10px" }}>Overall risk score: {overallRiskScore}/100</h2>
        </div>
        <div style={{ alignSelf: "center", color: "#6b7280" }}>{cached ? "Served from cache" : "Fresh Claude analysis"}</div>
      </div>
      <p>{executiveSummary}</p>
      <p><strong>Negotiation stance:</strong> {negotiationSummary}</p>
    </section>
  );
}

RiskBanner.propTypes = {
  overallRisk: PropTypes.string.isRequired,
  overallRiskScore: PropTypes.number.isRequired,
  executiveSummary: PropTypes.string.isRequired,
  negotiationSummary: PropTypes.string.isRequired,
  cached: PropTypes.bool,
};

RiskBanner.defaultProps = {
  cached: false,
};
