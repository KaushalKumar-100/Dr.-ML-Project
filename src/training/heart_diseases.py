import os
import logging
from pathlib import Path

from dotenv import load_dotenv
from joblib import dump
import  pandas as pd
import yaml

from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    recall_score,
    f1_score
)


def heart_model():
    try:
        #load env file content to env variables
        load_dotenv()
        
        PROJECT_ROOT=Path(os.getenv("PROJECT_ROOT")).resolve()
        
        DATASET_PATH=(PROJECT_ROOT 
                     / os.getenv("DATASET_DIR")
                     / os.getenv("HEART_DATASET_PATH")
                    )
        MODEL_PATH=(PROJECT_ROOT
                    /os.getenv('MODEL_DIR')
                    / os.getenv("HEART_DISEASE_MODEL_PATH")
                    )
        LOG_PATH=(PROJECT_ROOT
                  / os.getenv("LOG_DIR")
                  / os.getenv("LOG_HEART_PATH"))
        
        HYPER_PARAMS_YAML_PATH = (PROJECT_ROOT
                    / os.getenv("HYPER_PARAMS_YAML_PATH")
                    )
        
        TARGET_COL=os.getenv("HEART_DISEASE_TARGET_COL")
        TEST_SIZE=float(os.getenv("TEST_SIZE"))
        RANDOM_STATE=int(os.getenv("RANDOM_STATE"))
        
        MODEL_PATH.parent.mkdir(parents=True,exist_ok=True)
        LOG_PATH.parent.mkdir(parents=True,exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(LOG_PATH)
            ]
        )
            
            
        df=pd.read_csv(DATASET_PATH)
        logging.info(f"Dataset Loaded with shape: {df.shape}")
        
        X=df.drop(columns=[TARGET_COL])
        y=df[TARGET_COL]

        row_signature=pd.util.hash_pandas_object(X,index=False)
        
        gss=GroupShuffleSplit(
            n_splits=1,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE
        )

        train_idx,test_idx=next(
            gss.split(X,y,groups=row_signature)
        )

        X_train,X_test=X.iloc[train_idx],X.iloc[test_idx]
        y_train,y_test=y.iloc[train_idx],y.iloc[test_idx]
        
        logging.info(f"Train shape {X_train.shape}, Test shape: {X_test.shape}")
        
        #Best parmas from Notebook
        with open (HYPER_PARAMS_YAML_PATH,'r') as file:
            hyperparams= yaml.safe_load(file)
            
        
        model_params=hyperparams['heart_disease']['params']
        best_rf=RandomForestClassifier(
            random_state=RANDOM_STATE,
            **model_params,
        )
                    
        
        pipeline=Pipeline(
            steps=[
                ('scaler',StandardScaler()),
                ("model",best_rf)
            ]
        )      
        
        pipeline.fit(X_train,y_train)
        logging.info("Model Training completed")
        # Evaluation
        y_train_pred = pipeline.predict(X_train)
        y_test_pred = pipeline.predict(X_test)

        train_acc = accuracy_score(y_train, y_train_pred)
        test_acc = accuracy_score(y_test, y_test_pred)

        train_recall = recall_score(y_train, y_train_pred)
        test_recall = recall_score(y_test, y_test_pred)

        train_f1= f1_score(y_train, y_train_pred)
        test_f1 = f1_score(y_test, y_test_pred)

        logging. info(f"Train Accuracy: {train_acc :.4f} | Recall: {train_recall :.4f} | F1: {train_f1 :.4f}")
        logging. info(f"Test Accuracy: {test_acc :.4f} | Recall: {test_recall :.4f} | F1: {test_f1 :.4f}")

        logging.info("Train Classification Report:\n" + classification_report(y_train, y_train_pred))
        logging.info("Test Classification Report:\n" + classification_report(y_test, y_test_pred))
                
        #sav trained model
        
        dump(pipeline,MODEL_PATH)
        logging.info(f"Model saved to :{MODEL_PATH}")
        logging.info("Training Scripts completed")
        
        
    except Exception as e:
        print(f"Training failed :{e}")
        logging.exception(f"Training Script Failed: {e}")
        
        
        
if __name__=="__main__":
    heart_model()