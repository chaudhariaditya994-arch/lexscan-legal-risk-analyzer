import React from 'react';

const ClauseCard = ({ clause }) => {
  return (
    <div className="clause-card">
      <h3>{clause.title}</h3>
      <p>Risk: {clause.risk}</p>
      <p>{clause.explanation}</p>
      <p>{clause.recommendation}</p>
    </div>
  );
};

export default ClauseCard;