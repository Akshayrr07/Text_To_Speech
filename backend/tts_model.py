from gtts import gTTS
import os
from backend.config import Config
import logging
import io

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TTSModel:
    def __init__(self):
        self.lang = "en"
        logger.info("TTS model initialized with gTTS")
    
    def synthesize(self, text: str) -> bytes:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        if len(text) > Config.MAX_TEXT_LENGTH:
            raise ValueError(f"Text too long. Max length: {Config.MAX_TEXT_LENGTH}")
        
        try:
            tts = gTTS(text=text, lang=self.lang, slow=False)
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            audio_bytes = audio_buffer.read()
            return audio_bytes
        except Exception as e:
            logger.error(f"Error during synthesis: {e}")
            raise

_tts_instance = None

def get_tts_model():
    global _tts_instance
    if _tts_instance is None:
        _tts_instance = TTSModel()
    return _tts_instance
