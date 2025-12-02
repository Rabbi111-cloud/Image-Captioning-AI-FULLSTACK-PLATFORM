from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from transformers import BlipProcessor, BlipForConditionalGeneration

app = FastAPI(title="Image Captioning AI API")

# Allow all frontend origins (Gradio, Colab, others)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once at startup
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    # Read image bytes
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Process image
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return {"caption": caption}

# Required for Render
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
