import React from "react";
import { Pressable, ScrollView, Text } from "react-native";

export default function ClauseDetailScreen({ clause, onBack }) {
  if (!clause) {
    return null;
  }

  return (
    <ScrollView contentContainerStyle={{ padding: 24, gap: 16 }}>
      <Pressable onPress={onBack}><Text style={{ color: "#1d4ed8" }}>Back</Text></Pressable>
      <Text style={{ fontSize: 28, fontWeight: "700" }}>{clause.title}</Text>
      <Text>{clause.category} · {clause.risk} · {clause.score}/100</Text>
      <Text>{clause.clauseText}</Text>
      <Text>{clause.explanation}</Text>
      <Text style={{ fontWeight: "700" }}>Recommendation</Text>
      <Text>{clause.recommendation}</Text>
    </ScrollView>
  );
}
