import React from 'react';

const RiskBanner = ({ result }) => {
  return (
    <div className="risk-banner">
      <h2>Overall Risk: {result.overallRisk}</h2>
      <p>High: {result.highCount}, Medium: {result.mediumCount}, Low: {result.lowCount}</p>
    </div>
  );
};

export default RiskBanner;