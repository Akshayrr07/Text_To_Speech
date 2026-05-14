from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.tts_model import get_tts_model
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="TTS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_path, "index.html"))

class TTSRequest(BaseModel):
    text: str

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/tts")
async def text_to_speech(request: TTSRequest):
    try:
        tts_model = get_tts_model()
        audio_bytes = tts_model.synthesize(request.text)
        return Response(content=audio_bytes, media_type="audio/wav")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"TTS error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate speech")
