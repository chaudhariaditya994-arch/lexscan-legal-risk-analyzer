import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export function useAnalyzer() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyze(file, userId = "demo-user") {
    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("userId", userId);

    try {
      const response = await fetch(`${API_BASE}/api/analyze`, {
        method: "POST",
        body: formData,
      });
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || "Analysis failed.");
      }
      return payload;
    } catch (requestError) {
      const message = requestError instanceof Error ? requestError.message : "Analysis failed.";
      setError(message);
      throw requestError;
    } finally {
      setLoading(false);
    }
  }

  return { analyze, loading, error };
}
