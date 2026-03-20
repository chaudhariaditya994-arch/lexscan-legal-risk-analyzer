import React, { useEffect } from "react";
import { ActivityIndicator, Text, View } from "react-native";

export default function AnalyzingScreen({ onComplete }) {
  useEffect(() => {
    const timer = setTimeout(onComplete, 1400);
    return () => clearTimeout(timer);
  }, [onComplete]);

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center", gap: 16 }}>
      <ActivityIndicator size="large" color="#1d4ed8" />
      <Text>Claude is reviewing the contract...</Text>
    </View>
  );
}
