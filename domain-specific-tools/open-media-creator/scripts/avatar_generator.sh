#!/bin/bash
# Reference Script for Avatar Generation (SadTalker / Wav2Lip)

echo "Open Source Avatar Generation Command Reference"
echo "-----------------------------------------------"
echo "Make sure you have cloned the respective repository and installed dependencies."
echo ""

# SadTalker Example
echo "[SadTalker Example]"
echo "python inference.py --driven_audio /path/to/audio.wav \"
echo "                    --source_image /path/to/image.png \"
echo "                    --result_dir ./results --still --preprocess full \"
echo "                    --enhancer gfpgan"
echo ""

# Wav2Lip Example
echo "[Wav2Lip Example]"
echo "python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth \"
echo "                    --face /path/to/video.mp4 \"
echo "                    --audio /path/to/audio.wav"
echo ""
echo "Note: The AI agent can adapt these commands based on the user's specific local setup."
