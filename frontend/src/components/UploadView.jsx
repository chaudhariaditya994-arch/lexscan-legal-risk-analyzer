import React from 'react';

const UploadView = ({ onUpload, onHistory }) => {
  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      // simulate upload
      onUpload({ clauses: [], overallRisk: 'LOW', highCount: 0, mediumCount: 0, lowCount: 0 });
    }
  };

  return (
    <div>
      <h1>Upload PDF Contract</h1>
      <input type="file" accept="application/pdf" onChange={handleFileUpload} />
      <button onClick={onHistory}>View History</button>
    </div>
  );
};

export default UploadView;