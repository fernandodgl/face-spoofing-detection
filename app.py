from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import io
import shutil

app = FastAPI()

# Load your trained model
model = load_model('model/model.h5')

@app.get('/')
def read_root():
    return {"message": "== Face Spoof Detection App Online =="}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check if the file extension is in the ALLOWED_EXTENSIONS set
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    file_extension = file.filename.rsplit(".", 1)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type. Must be .png, .jpg, or .jpeg")

    # Open Image and make sure it's RGB
    try:
        image = Image.open(file.file).convert('RGB')
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong while reading the file")

    # Resize image to expected input size
    image = image.resize((224, 224))

    # Convert Image to numpy array and normalize
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = np.vstack([image])
    image = image.astype('float32') / 255.0

    # Make prediction
    prediction = model.predict(image)
    prediction_label = 'Real' if prediction[0][0] < 0.65 else 'Fake'

    # Save the image to disk
    image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "prediction": prediction_label,
        "image": image_path
    }
