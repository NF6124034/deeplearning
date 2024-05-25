from Xray.exception import XRayException
from Xray.pipeline.training_pipeline import TrainingPipeline
import sys

def start_training():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        
    except Exception as e:
        raise XRayException(e, sys)
    
if __name__ == "__main__":
    start_training()