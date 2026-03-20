import React from "react";
import { Pressable, ScrollView, Text, View } from "react-native";

export default function ResultScreen({ result, onOpenClause, onOpenHistory }) {
  return (
    <ScrollView contentContainerStyle={{ padding: 24, gap: 16 }}>
      <Text style={{ fontSize: 28, fontWeight: "700" }}>{result.documentTitle}</Text>
      <Text style={{ fontSize: 16 }}>Overall risk: {result.overallRisk} ({result.overallRiskScore}/100)</Text>
      <Text style={{ color: "#475569" }}>{result.executiveSummary}</Text>
      {result.clauses.map((clause) => (
        <Pressable key={clause.title} onPress={() => onOpenClause(clause)} style={{ backgroundColor: "white", padding: 16, borderRadius: 18, gap: 8 }}>
          <Text style={{ fontWeight: "700" }}>{clause.title}</Text>
          <Text>{clause.category} · {clause.risk}</Text>
          <Text style={{ color: "#475569" }}>{clause.explanation}</Text>
        </Pressable>
      ))}
      <Pressable onPress={onOpenHistory} style={{ padding: 16, borderRadius: 14, backgroundColor: "#e2e8f0" }}>
        <Text style={{ textAlign: "center", fontWeight: "700" }}>Open History</Text>
      </Pressable>
    </ScrollView>
  );
}
