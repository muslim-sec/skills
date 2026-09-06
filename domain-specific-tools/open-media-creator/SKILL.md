---
name: open-media-creator
description: Generates open-source and API-agnostic scripts/workflows for creating TTS audio, AI images, generated video, and lip-synced avatars using local models or generic generic APIs.
---

# Open Media Creator Skill

Use this skill when the user wants to generate multimedia (Audio, Video, Images, Avatars) using open-source tools, local models, or generic non-vendor-locked APIs.

## Supported Modalities

### 1. Text-to-Speech (TTS)
- **Local / Free Edge TTS**: Use the included `scripts/tts_generator.py` (which uses the `edge-tts` python package) for free, high-quality human voices. 
- **API Mode**: Instruct the agent to write scripts calling generic endpoints (e.g., ElevenLabs, OpenAI TTS) if the user provides an API key.

### 2. AI Avatars & Lip-sync
- **Local Models**: Recommend and write CLI commands to run open-source repositories like [SadTalker](https://github.com/OpenTalker/SadTalker) or [Wav2Lip](https://github.com/Rudrabha/Wav2Lip). Use `scripts/avatar_generator.sh` for reference commands.
- **API Mode**: Write generic API requests for services like D-ID or HeyGen if the user provides keys.

### 3. Image Generation
- **Local Models (Stable Diffusion / ComfyUI)**: Write scripts that hit `http://127.0.0.1:8188/prompt` for ComfyUI or `http://127.0.0.1:7860/sdapi/v1/txt2img` for A1111.
- **API Mode**: Write OpenAI-compatible payload scripts for text-to-image generation.

### 4. Video Generation & Manipulation
- **FFMPEG Automation**: Write FFMPEG scripts for merging audio, video, adding subtitles, and compositing avatars.
- **Open Video Models**: Provide instructions or API calls for open video models (e.g., AnimateDiff).

## Execution Guidelines
1. **Always ask for the environment**: Does the user have a powerful GPU (for local execution) or do they prefer lightweight Python scripts/free APIs?
2. **Never lock the user**: Do not hardcode specific paid vendor MCPs or require closed platforms unless explicitly requested.
3. **Execution**: You can execute the Python and Bash scripts in the `scripts/` folder on behalf of the user using terminal commands if the dependencies (`edge-tts`, `ffmpeg`) are installed.
