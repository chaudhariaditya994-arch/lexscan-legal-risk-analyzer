import React from 'react';
import ClauseCard from './ClauseCard';
import RiskBanner from './RiskBanner';

const ResultView = ({ result, onBack }) => {
  return (
    <div>
      <button onClick={onBack}>Back</button>
      <RiskBanner result={result} />
      {result.clauses.map((clause, index) => (
        <ClauseCard key={index} clause={clause} />
      ))}
    </div>
  );
};

export default ResultView;