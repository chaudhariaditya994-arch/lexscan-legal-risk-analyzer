export const toolSchema = {
  type: 'function',
  function: {
    name: 'analyze_legal_document',
    description: 'Analyze a legal document for risky clauses',
    parameters: {
      type: 'object',
      properties: {
        clauses: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              title: { type: 'string' },
              risk: { type: 'string', enum: ['HIGH', 'MEDIUM', 'LOW'] },
              explanation: { type: 'string' },
              recommendation: { type: 'string' },
            },
            required: ['title', 'risk', 'explanation', 'recommendation'],
          },
        },
        overallRisk: { type: 'string' },
      },
      required: ['clauses', 'overallRisk'],
    },
  },
};