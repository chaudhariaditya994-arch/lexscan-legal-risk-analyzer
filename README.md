# ? LEXSCAN — AI Legal Risk Analyzer

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![MongoDB](https://img.shields.io/badge/MongoDB-motor-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Anthropic Claude](https://img.shields.io/badge/Anthropic-Claude%20Sonnet%204-D97706)](https://www.anthropic.com/)
[![CI](https://github.com/chaudhariaditya994-arch/lexscan-legal-risk-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/chaudhariaditya994-arch/lexscan-legal-risk-analyzer/actions/workflows/ci.yml)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

AI-powered legal document risk analyzer — upload any PDF contract and Claude AI identifies risky clauses, flags hidden traps, and explains them in plain English.

## Features

- Upload any PDF contract (offer letter, lease, NDA, SaaS terms)
- Claude AI reads the full document natively — no OCR needed
- Identifies 6–15 risky clauses per document
- Flags: Auto-renewal traps, One-sided termination, Hidden penalties, Forced arbitration, IP assignment, Non-compete clauses
- Risk meter: HIGH / MEDIUM / LOW per clause
- Plain English explanation + negotiation recommendation per clause
- Web search tool — looks up unfamiliar legal terms in real time
- In-memory MongoDB session history
- Export PDF risk report

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | React, Vite |
| AI Engine | Claude Sonnet via Anthropic API (tool_use + web_search) |
| Backend | FastAPI, Python 3.11 |
| Database | MongoDB (motor async driver) |
| Cache | Redis (SHA256 PDF deduplication) |
| Mobile | Expo React Native |
| PDF Generation | ReportLab |
| Auth | Google OAuth 2.0 + JWT |

## How tool_use Works

LEXSCAN defines a custom client tool called `analyze_legal_document`. The backend forces Claude to finish by calling that tool and returning structured JSON instead of unstructured prose. The schema includes document metadata, overall risk, a clause list, searched legal terms, and negotiation guidance. Because the request also enables the `web_search_20250305` server tool, Claude can look up unfamiliar legal terms before it submits the final tool payload.

Shared schema references live in:

- `frontend/src/utils/toolSchema.js`
- `backend/models/analysis.py`
- `backend/services/claude_service.py`

## Quickstart

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Mobile

```bash
cd mobile
npm install
npm run start
```

### Sample Contract Generator

```bash
python scripts/generate_sample_contract.py
```

## Environment Variables

| Variable | Required | Description |
| --- | --- | --- |
| `ANTHROPIC_API_KEY` | Yes | Anthropic API key for Claude analysis |
| `ANTHROPIC_MODEL` | No | Defaults to `claude-sonnet-4-20250514` |
| `MONGODB_URI` | No | Async MongoDB connection string |
| `MONGODB_DATABASE` | No | MongoDB database name |
| `REDIS_URL` | No | Redis URL for SHA256 PDF deduplication |
| `GOOGLE_CLIENT_ID` | No | Google OAuth client ID |
| `JWT_SECRET_KEY` | Yes | Secret used to sign JWT access tokens |
| `JWT_EXPIRE_MINUTES` | No | JWT expiration in minutes |
| `CORS_ORIGINS` | No | Comma-separated frontend origins |
| `APP_ENV` | No | Environment label such as `development` or `production` |

## Author

Aditya Chaudhary (`chaudhariaditya994-arch`)

## License

MIT License
