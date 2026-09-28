# 🧾 Evaluation – Milestone 4 (Translation API)

**Evaluation week:** 8

## Criteria and status

| Criterion | Target | Status |
|---|---|---|
| Working API endpoint | `POST /translate` | ✅ Implemented (`deploy_app.py`) |
| Health check and error handling | Yes | ✅ `/health`, validation, 502 on service errors |
| Cloud deployment | Azure App Service / Container | ⏳ Future work |
| OTT player integration | Prototype | ⏳ Future work |
| Low end-to-end latency | < 3 s | 🔄 Not yet benchmarked |

## Deliverables
1. API code: `src/deploy_app.py`
2. Run instructions and example request: `milestone4.md`

## How to verify
```bash
uvicorn src.deploy_app:app --reload
```
Open `http://127.0.0.1:8000/docs`, try `POST /translate`, and confirm a translation is returned.

## Summary
The API prototype works locally. Cloud deployment and OTT integration are planned next steps.
