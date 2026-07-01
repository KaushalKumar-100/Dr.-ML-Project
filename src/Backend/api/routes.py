from fastapi import APIRouter

from src.Backend.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse
)

from src.Backend.services.predictor import predict_diseases


router=APIRouter()

@router.get("/healt")
def health_check():
    return {
        "status":"ok",
        "message":"API is runnig.."
    }
    
    
@router.post("/predict",response_model=PredictionResponse)
def predict_endpoint(request:PredictionRequest): 
    disease=request.disease
    features=request.features
    result=predict_diseases(
        disease=disease,
        input_data=features
    )
    return PredictionResponse(**result)