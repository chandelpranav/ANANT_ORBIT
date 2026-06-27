from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI(
    title="AI Enabled Exoplanet Detection",
    version="1.0"
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():

    return {
        "Project":"AI Enabled Exoplanet Detection",
        "Team":"ANANT ORBIT",
        "Status":"Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    # Dummy prediction
    prediction = {
        "Target":file.filename,
        "Prediction":"Planet Detected",
        "Confidence":"98.7%",
        "Estimated Radius":"1.18 Earth Radius",
        "Transit Depth":"0.0021",
        "Orbital Period":"18.12 Days"
    }

    return JSONResponse(prediction)