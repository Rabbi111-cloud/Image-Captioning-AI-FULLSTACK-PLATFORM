# README.md
readme_content = """
# Image Captioning AI - Fullstack

## Description
Cloud-based full-stack Image Captioning AI using Hugging Face BLIP. 
Frontend: Gradio. Backend: FastAPI. Deployment: Render free tier.

## Setup
1. Run frontend.ipynb in Google Colab.
2. Run backend app.py locally or deploy on Render.
3. Gradio UI calls backend API for captions.
"""
with open("README.md","w") as f:
    f.write(readme_content)
