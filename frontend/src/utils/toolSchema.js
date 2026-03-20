export const analyzeLegalDocumentSchema = {
  name: "analyze_legal_document",
  description: "Return structured legal risk findings for a contract or agreement.",
  input_schema: {
    type: "object",
    additionalProperties: false,
    properties: {
      documentTitle: { type: "string" },
      documentType: { type: "string" },
      overallRisk: { type: "string", enum: ["HIGH", "MEDIUM", "LOW"] },
      overallRiskScore: { type: "integer", minimum: 0, maximum: 100 },
      executiveSummary: { type: "string" },
      negotiationSummary: { type: "string" },
      searchedLegalTerms: {
        type: "array",
        items: { type: "string" },
      },
      clauses: {
        type: "array",
        minItems: 6,
        maxItems: 15,
        items: {
          type: "object",
          additionalProperties: false,
          properties: {
            title: { type: "string" },
            category: { type: "string" },
            risk: { type: "string", enum: ["HIGH", "MEDIUM", "LOW"] },
            score: { type: "integer", minimum: 0, maximum: 100 },
            clauseText: { type: "string" },
            explanation: { type: "string" },
            recommendation: { type: "string" },
          },
          required: [
            "title",
            "category",
            "risk",
            "score",
            "clauseText",
            "explanation",
            "recommendation"
          ]
        }
      }
    },
    required: [
      "documentTitle",
      "documentType",
      "overallRisk",
      "overallRiskScore",
      "executiveSummary",
      "negotiationSummary",
      "searchedLegalTerms",
      "clauses"
    ]
  }
};
