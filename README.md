---
title: Text-to-Speech Web App
emoji: 🎙️
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
license: mit
---

# Text-to-Speech Web Application

Lightweight, low-latency TTS system using Google TTS (gTTS).

## Features
- English-only text-to-speech
- Single voice output
- Optimized for short phrases
- FastAPI backend
- Minimal HTML/CSS/JS frontend
- HuggingFace Spaces deployment ready

## Architecture
- **Model**: Google TTS (gTTS)
- **Backend**: FastAPI
- **Frontend**: Lightweight HTML/CSS/JS
- **Deployment**: HuggingFace Spaces (Docker)

## Local Setup
```bash
pip install -r requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port 7860
```

## HuggingFace Spaces Deployment

### Step 1: Create Space
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Name: `text-to-speech-app`
4. Select "Docker" as SDK
5. Make it Public

### Step 2: Upload Files
Upload all files from this project to the Space:
- `backend/`
- `frontend/`
- `requirements.txt`
- `Dockerfile`
- `app.py`
- `README.md`

### Step 3: Auto-Deploy
The Space will automatically build and deploy the Docker container.

### Step 4: Access
Once deployed, access at: `https://huggingface.co/spaces/YOUR_USERNAME/text-to-speech-app`

## API Endpoints
- `GET /` - Frontend UI
- `POST /api/tts` - Generate speech from text
- `GET /health` - Health check
