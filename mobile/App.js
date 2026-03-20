import React, { useMemo, useState } from "react";
import { SafeAreaView, View } from "react-native";
import HomeScreen from "./screens/HomeScreen";
import AnalyzingScreen from "./screens/AnalyzingScreen";
import ResultScreen from "./screens/ResultScreen";
import ClauseDetailScreen from "./screens/ClauseDetailScreen";
import HistoryScreen from "./screens/HistoryScreen";

const mockResult = {
  documentTitle: "TechNova Offer Letter",
  overallRisk: "HIGH",
  overallRiskScore: 88,
  executiveSummary: "The offer is heavily employer-favoring and contains multiple high-friction clauses.",
  clauses: [
    {
      title: "Global non-compete",
      category: "Employment Restriction",
      risk: "HIGH",
      score: 94,
      clauseText: "Employee shall not work for any competing enterprise worldwide for 36 months.",
      explanation: "This broad restraint can block future work opportunities.",
      recommendation: "Ask to narrow the geography, duration, and scope.",
    }
  ]
};

export default function App() {
  const [screen, setScreen] = useState("home");
  const [selectedClause, setSelectedClause] = useState(null);

  const content = useMemo(() => {
    if (screen === "analyzing") {
      return <AnalyzingScreen onComplete={() => setScreen("result")} />;
    }
    if (screen === "result") {
      return <ResultScreen result={mockResult} onOpenClause={(clause) => { setSelectedClause(clause); setScreen("clause"); }} onOpenHistory={() => setScreen("history")} />;
    }
    if (screen === "clause") {
      return <ClauseDetailScreen clause={selectedClause} onBack={() => setScreen("result")} />;
    }
    if (screen === "history") {
      return <HistoryScreen items={[mockResult]} onBack={() => setScreen("result")} />;
    }
    return <HomeScreen onAnalyze={() => setScreen("analyzing")} />;
  }, [screen, selectedClause]);

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: "#f8fafc" }}>
      <View style={{ flex: 1 }}>{content}</View>
    </SafeAreaView>
  );
}
