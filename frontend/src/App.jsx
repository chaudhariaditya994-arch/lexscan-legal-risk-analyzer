import React, { useState } from 'react';
import UploadView from './components/UploadView';
import ResultView from './components/ResultView';
import HistoryView from './components/HistoryView';
import './App.css';

function App() {
  const [view, setView] = useState('upload');
  const [analysisResult, setAnalysisResult] = useState(null);

  const handleUpload = (result) => {
    setAnalysisResult(result);
    setView('result');
  };

  const handleBack = () => {
    setView('upload');
  };

  const handleHistory = () => {
    setView('history');
  };

  return (
    <div className="App">
      {view === 'upload' && <UploadView onUpload={handleUpload} onHistory={handleHistory} />}
      {view === 'result' && <ResultView result={analysisResult} onBack={handleBack} />}
      {view === 'history' && <HistoryView onBack={handleBack} />}
    </div>
  );
}

export default App;