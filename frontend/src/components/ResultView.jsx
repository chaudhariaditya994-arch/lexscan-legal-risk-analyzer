import PropTypes from "prop-types";
import ClauseCard from "./ClauseCard";
import RiskBanner from "./RiskBanner";

export default function ResultView({ result }) {
  return (
    <section style={{ display: "grid", gap: 18 }}>
      <RiskBanner
        overallRisk={result.overallRisk}
        overallRiskScore={result.overallRiskScore}
        executiveSummary={result.executiveSummary}
        negotiationSummary={result.negotiationSummary}
        cached={result.cached}
      />
      <section style={{ background: "#fff", borderRadius: 24, padding: 24 }}>
        <h3 style={{ marginTop: 0 }}>{result.documentTitle}</h3>
        <p>{result.documentType}</p>
        <p><strong>Searched terms:</strong> {result.searchedLegalTerms?.join(", ") || "None"}</p>
      </section>
      <section style={{ display: "grid", gap: 14 }}>
        {result.clauses.map((clause) => (
          <ClauseCard key={`${clause.title}-${clause.category}`} clause={clause} />
        ))}
      </section>
    </section>
  );
}

ResultView.propTypes = {
  result: PropTypes.shape({
    documentTitle: PropTypes.string.isRequired,
    documentType: PropTypes.string.isRequired,
    overallRisk: PropTypes.string.isRequired,
    overallRiskScore: PropTypes.number.isRequired,
    executiveSummary: PropTypes.string.isRequired,
    negotiationSummary: PropTypes.string.isRequired,
    searchedLegalTerms: PropTypes.arrayOf(PropTypes.string),
    clauses: PropTypes.arrayOf(PropTypes.object).isRequired,
    cached: PropTypes.bool,
  }).isRequired,
};
