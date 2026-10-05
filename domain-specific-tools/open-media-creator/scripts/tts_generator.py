#!/usr/bin/env python3
import asyncio
import edge_tts
import sys
import argparse

async def generate_tts(text, voice, output_file):
    print(f"Generating audio using voice: {voice}...")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"Audio saved successfully to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Free TTS Generator using edge-tts")
    parser.add_argument("--text", required=True, help="Text to convert to speech")
    parser.add_argument("--voice", default="en-US-AriaNeural", help="Voice model (e.g., en-US-AriaNeural, en-GB-SoniaNeural, ar-EG-SalmaNeural)")
    parser.add_argument("--output", default="output.mp3", help="Output MP3 file path")
    args = parser.parse_args()

    asyncio.run(generate_tts(args.text, args.voice, args.output))
