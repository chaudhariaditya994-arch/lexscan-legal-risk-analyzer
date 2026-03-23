import React from 'react';

const HistoryView = ({ onBack }) => {
  return (
    <div>
      <button onClick={onBack}>Back</button>
      <h1>Analysis History</h1>
      {/* list history */}
    </div>
  );
};

export default HistoryView;