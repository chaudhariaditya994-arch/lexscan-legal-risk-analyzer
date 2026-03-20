import React from "react";
import { Pressable, ScrollView, Text, View } from "react-native";

export default function HistoryScreen({ items, onBack }) {
  return (
    <ScrollView contentContainerStyle={{ padding: 24, gap: 16 }}>
      <Pressable onPress={onBack}><Text style={{ color: "#1d4ed8" }}>Back</Text></Pressable>
      <Text style={{ fontSize: 28, fontWeight: "700" }}>History</Text>
      {items.map((item) => (
        <View key={item.documentTitle} style={{ backgroundColor: "white", padding: 16, borderRadius: 18 }}>
          <Text style={{ fontWeight: "700" }}>{item.documentTitle}</Text>
          <Text>{item.overallRisk} · {item.overallRiskScore}/100</Text>
        </View>
      ))}
    </ScrollView>
  );
}
