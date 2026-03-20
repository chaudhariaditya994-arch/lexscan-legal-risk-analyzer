# API Documentation

## Endpoints

### POST `/api/analyze`

Uploads a PDF contract and returns structured risk analysis.

Form fields:

- `file`: required PDF upload
- `userId`: optional user identifier

Response includes:

- `cached`
- `processingTimeMs`
- `overallRisk`
- `clauses`

### GET `/api/history/{userId}`

Returns recent history for a user.

### DELETE `/api/history/{userId}`

Deletes all stored sessions for a user.

### GET `/api/report/pdf/{id}`

Builds and streams a ReportLab PDF risk report.

### POST `/auth/google`

Accepts a Google credential token and returns a signed JWT plus user profile.
