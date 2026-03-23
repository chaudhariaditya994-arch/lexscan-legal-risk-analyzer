# ⚖ LEXSCAN — AI Legal Risk Analyzer

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)

[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)

[![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green.svg)](https://www.mongodb.com/)

[![Anthropic Claude](https://img.shields.io/badge/Anthropic-Claude-orange.svg)](https://www.anthropic.com/)

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI-powered legal document risk analyzer — upload any PDF contract and Claude AI identifies risky clauses, flags hidden traps, and explains them in plain English.

## Features

- **Upload any PDF contract** (offer letter, lease, NDA, SaaS terms)
- **Claude AI reads the full document natively** — no OCR needed
- **Identifies 6–15 risky clauses per document**
- **Flags**: Auto-renewal traps, One-sided termination, Hidden penalties, Forced arbitration, IP assignment, Non-compete clauses
- **Risk meter**: HIGH / MEDIUM / LOW per clause
- **Plain English explanation + negotiation recommendation per clause**
- **Web search tool** — looks up unfamiliar legal terms in real time
- **In-memory MongoDB session history**
- **Export PDF risk report**

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React, Vite |
| AI Engine | Claude Sonnet via Anthropic API (tool_use + web_search) |
| Backend | FastAPI, Python 3.11 |
| Database | MongoDB (motor async driver) |
| Cache | Redis (SHA256 PDF deduplication) |
| Mobile | Expo React Native |
| PDF Generation | ReportLab |
| Auth | Google OAuth 2.0 + JWT |

## How tool_use works

The system uses Claude's tool_use capability with a custom `analyze_legal_document` function. The tool schema defines parameters for document analysis, including risk categories and explanation requirements. Claude calls this tool to systematically analyze each clause, assign risk levels, and provide plain English explanations.

## Quickstart

### Backend

1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Set up environment variables (copy .env.example to .env and fill in values)

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

## Environment Variables

| Variable | Description |
|----------|-------------|
| ANTHROPIC_API_KEY | Your Anthropic API key |
| MONGODB_URI | MongoDB connection string |
| REDIS_URL | Redis connection URL |
| GOOGLE_CLIENT_ID | Google OAuth client ID |
| GOOGLE_CLIENT_SECRET | Google OAuth client secret |
| JWT_SECRET | JWT signing secret |

## Author

Aditya Chaudhary (chaudhariaditya994-arch)

## License

MIT