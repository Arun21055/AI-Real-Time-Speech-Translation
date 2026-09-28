# 🚀 Milestone 4 – Translation API (Deployment Prototype)

| | |
|---|---|
| **Duration** | Weeks 7–8 |
| **Status** | 🔄 Prototype: API built and runs locally; cloud deployment and OTT integration are future work |
| **Code** | `src/deploy_app.py` |

## Objective
Expose the translation module as a web API so other applications (for example an OTT player) can request translations.

## Tasks
- ✅ Built a **FastAPI** service with `GET /`, `GET /health` and `POST /translate`.
- ✅ Added input validation and error handling (empty text → 400, service failure → 502).
- ✅ Credentials are read from environment variables.
- 🔄 Cloud deployment (Azure App Service / Container Apps): **planned, not yet done**.
- 🔄 OTT player integration: **planned, not yet done**.

## Tools & Technologies
- FastAPI, Uvicorn, Pydantic
- Azure OpenAI

## Run locally
```bash
uvicorn src.deploy_app:app --reload
```
Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Example request
```bash
curl -X POST "http://127.0.0.1:8000/translate" \
     -H "Content-Type: application/json" \
     -d '{"text": "Welcome to the match!", "target_lang": "es"}'
```

## Example response
```json
{
  "translated_text": "¡Bienvenidos al partido!",
  "target_lang": "es",
  "status": "success"
}
```

## Planned deployment steps
1. Containerise the app with Docker.
2. Deploy the container to Azure App Service or Azure Container Apps.
3. Store keys in the platform's secret settings, not in code.
4. Connect an OTT player prototype to the `/translate` endpoint.

⬅️ [Milestone 3](milestone3.md)
