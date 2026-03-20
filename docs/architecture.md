# LEXSCAN Architecture

## Overview

LEXSCAN is split into a React frontend, a FastAPI backend, and an Expo mobile client. The backend owns AI orchestration, auth, caching, reporting, and persistence.

## Request Flow

1. A user uploads a PDF from web or mobile.
2. FastAPI computes a SHA256 hash for the file.
3. Redis is checked for a cached response.
4. On a miss, the backend sends the PDF to Claude Sonnet 4 using a PDF document block.
5. Claude may use `web_search_20250305` for unfamiliar legal terms.
6. Claude is forced to call `analyze_legal_document` with structured JSON.
7. MongoDB stores the completed analysis for history and export.
8. Frontend and mobile clients render the shared response shape.

## Components

### Frontend

- `UploadView` handles drag-and-drop uploads
- `ResultView` renders the analysis and clause breakdown
- `HistoryView` shows prior sessions
- `useAnalyzer` coordinates API calls and status state

### Backend

- `routers/analyze.py` handles upload validation and orchestration
- `services/claude_service.py` wraps Anthropic tool use
- `services/mongo_service.py` handles async persistence
- `services/cache_service.py` handles Redis cache keys and TTL
- `services/pdf_service.py` creates printable reports
- `middleware/rate_limit.py` implements free and pro tier limits

### Mobile

- `HomeScreen` triggers uploads
- `AnalyzingScreen` shows progress
- `ResultScreen` presents summary and clauses
- `HistoryScreen` reads prior analysis records
