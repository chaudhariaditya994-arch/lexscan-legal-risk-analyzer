import { useState } from 'react';

const useAnalyzer = () => {
  const [loading, setLoading] = useState(false);

  const analyze = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    const response = await fetch('/api/analyze', {
      method: 'POST',
      body: formData,
    });
    const result = await response.json();
    setLoading(false);
    return result;
  };

  return { analyze, loading };
};

export default useAnalyzer;