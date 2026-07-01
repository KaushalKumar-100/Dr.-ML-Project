from fastapi import FastAPI
from src.Backend.api.routes import router


app=FastAPI(
    title="Dr.ML Prediction App",
    version='1.0.0.2',
    description="Multi-Diseases Prediction Backend"
)

app.include_router(router,prefix="/api")
