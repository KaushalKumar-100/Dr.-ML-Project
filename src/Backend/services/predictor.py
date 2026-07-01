import os
import logging
from pathlib import Path
from dotenv import load_dotenv

from joblib import load
import  pandas as pd
from src.Backend.config.setting import Settings
from src.common.preprocessing_util import replace_zeros_with_nan


load_dotenv()
PROJECT_ROOT=Path(os.getenv("PROJECT_ROOT"))

MODEL_PATH= Path(PROJECT_ROOT
            /os.getenv('MODEL_DIR')
        )

DIABETES_MODEL_PATH=(MODEL_PATH
            /os.getenv("DIABETES_MODEL_PATH")
            )

HEART_MODEL_PATH=(MODEL_PATH
            /os.getenv("HEART_DISEASE_MODEL_PATH")
            )


LOG_PATH=(PROJECT_ROOT
          / os.getenv("LOG_DIR")
          )


LOG_PREDICTOR_PATH=(LOG_PATH
                / os.getenv("LOG_PREDICTOR_PATH")
                )

LOG_PREDICTOR_PATH.parent.mkdir(parents=True,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_PREDICTOR_PATH)
    ]
)

#loading the model once
logging.info("loading trained Model...")
diabetes_model=load(DIABETES_MODEL_PATH)
heart_model=load(HEART_MODEL_PATH)
logging.info("Models loaded Completed ....")


#common prediction functions
def predict_diseases(disease:str,input_data:dict):
    
    if disease=="diabetes":
        model=diabetes_model
        
        
    elif disease=="heart_diseases":
        model=heart_model
        
    else:
        raise ValueError("Invalid Diseases Type : use diabetes or heart diseases")
    
    
    x_df=pd.DataFrame([input_data])
    prediction =int(model.predict(x_df)[0])
    
    #probability for positive class
    
    probability=float(model.predict_proba(x_df)[0][1])
    
    logging.info(
        f"[{disease}] prediction ={prediction} , probability= {probability} "
        
    )
    return {
        "disease":disease,
        "prediction":prediction,
        "probability":probability,
    }
     
# diabetes_input = {
#     "Pregnancies": 2,
#     "Glucose": 120,
#     "BloodPressure": 70,
#     "SkinThickness": 25,
#     "Insulin": 80,
#     "BMI": 28.5,
#     "DiabetesPedigreeFunction": 0.5,
#     "Age": 30

# }

# heart_input = {
#     "age": 52,
#     "sex": 1,
#     "cp": 0,
#     "trestbps": 125,
#     "chol": 212,
#     "fbs": 0,
#     "restecg": 1,
#     "thalach": 168,
#     "exang": 0,
#     "oldpeak": 1.0,
#     "slope": 2,
#     "ca": 0,
#     "thal": 2
# }

# print(predict_diseases("diabetes", diabetes_input))
# print(predict_diseases("heart_diseases", heart_input))