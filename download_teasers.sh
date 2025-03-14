#!/bin/bash

# Create directory if it doesn't exist
mkdir -p assets/teaser

# Download CurricuVLM teaser
curl -o assets/teaser/sheng_curricuvlm.gif https://zihaosheng.github.io/CurricuVLM/static/images/case3-trained-combined.gif

# Download VLM-RL teaser
curl -o assets/teaser/huang_vlmrl.gif https://raw.githubusercontent.com/zilin-huang/VLM-RL-website/master/static/videos/CLIP/CLIP_town2_normal/CLIP_town2_normal_s6.gif

echo "Teaser images downloaded successfully!" 