"""
Milestone 4 - Deployment API for Real-Time Translation
This FastAPI app exposes a REST endpoint for text translation.
Run locally: uvicorn src.deploy_app:app --reload   (then open http://127.0.0.1:8000/docs)
"""
 
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AzureOpenAI
 
app = FastAPI(title="AI Speech Translation API", version="1.1")
 
# ---------- CONFIGURATION ----------
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_AZURE_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")  # your deployment name
 
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-06-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)
 
 
# ---------- INPUT MODEL ----------
class TranslationRequest(BaseModel):
    text: str
    target_lang: str
 
 
# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "AI Translation API is running"}
 
 
@app.get("/health")
def health():
    return {"status": "ok"}
 
 
@app.post("/translate")
def translate_text(req: TranslationRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text must not be empty")
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            temperature=0.2,
            messages=[
                {"role": "system", "content":
                    f"Translate the user's text to {req.target_lang}. Reply with ONLY the translation."},
                {"role": "user", "content": req.text},
            ],
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Translation service error: {exc}")
 
    translation = response.choices[0].message.content.strip()
    return {"translated_text": translation, "target_lang": req.target_lang, "status": "success"}
 
