import React from "react";
import { Pressable, Text, View } from "react-native";

export default function HomeScreen({ onAnalyze }) {
  return (
    <View style={{ flex: 1, padding: 24, justifyContent: "center", gap: 16 }}>
      <Text style={{ fontSize: 34, fontWeight: "700" }}>LEXSCAN</Text>
      <Text style={{ fontSize: 16, color: "#475569" }}>Upload or share a PDF contract to get instant clause-level risk analysis.</Text>
      <Pressable onPress={onAnalyze} style={{ backgroundColor: "#1d4ed8", padding: 16, borderRadius: 14 }}>
        <Text style={{ color: "white", textAlign: "center", fontWeight: "700" }}>Analyze Contract</Text>
      </Pressable>
    </View>
  );
}
