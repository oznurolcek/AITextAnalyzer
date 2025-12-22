import os
import json

from dotenv import load_dotenv

from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai

# --------------------------------------------------
# ENV
# --------------------------------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# Gemini Client
# --------------------------------------------------
client = genai.Client(api_key=GEMINI_API_KEY)

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Models
# --------------------------------------------------
class TextRequest(BaseModel):
    text: str

# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.get("/")
def root():
    return {"message": "Backend çalışıyor 🎉"}

@app.post("/analyze")
def analyze_text(request: TextRequest):
    prompt = f"""
You are an AI text analysis assistant.

Analyze the following text.

Text:
\"\"\"{request.text}\"\"\"

Tasks:
1. Write a short summary.
2. Determine the sentiment as one of: positive, neutral, or negative.
3. Extract up to 5 relevant keywords.

IMPORTANT RULES:
- Respond in the SAME LANGUAGE as the input text.
- Return ONLY valid JSON.
- Do NOT include explanations or extra text.

JSON format:
{{
  "summary": "...",
  "sentiment": "positive | neutral | negative",
  "keywords": ["...", "..."]
}}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        raw_text = response.text.strip()
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(raw_text)
        return parsed

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="AI did not return valid JSON"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@app.get("/ai-test")
def ai_test():
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents="Merhaba Gemini, çalışıyor musun?"
    )
    return {"reply": response.text}

