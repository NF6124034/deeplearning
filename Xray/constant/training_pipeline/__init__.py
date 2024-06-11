from datetime import datetime
from typing import List

import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

####################################


## Data Ingestion Constants
ARTIFACT_DIR: str = "artifact"

BUCKET_NAME: str = "testing0524"

S3_DATA_FOLDER: str = "data"


### Data transformation constants

CLASS_LABEL_1: str="NORMAL"

CLASS_LABEL_2: str="PNEUMONIA"

BRIGHTNESS: float = 0.10

CONTRAST: float = 0.10

SATURATION: float = 0.10

HUE: float = 0.10

RESIZE: int = 224

CENTERCROP: int = 224

RANDOMROTATION: int = 10

NORMALIZE_LIST_1: List[float] = [0.485, 0.456, 0.406]

NORMALIZE_LIST_2: List[float] = [0.229, 0.224, 0.225]

TRAIN_TRANSFORMS_KEY: str = "xray_train_transforms"

TRAIN_TRANSFORMATION_FILE: str = "train_transforms.pkl"

TEST_TRANSFORMS_FILE: str = "test_transforms.pkl"

BATCH_SIZE: int = 2

SHUFFLE: bool = False

PIN_MEMORY: bool = True


#model trainer constants

TRAINED_MODEL_DIR: str = "trained_model"

TRAINED_MODEL_NAME: str = "model.pt"

DEVICE: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

STEP_SIZE: int = 6

GAMMA: int = 0.5

EPOCH: int = 1

BENTOML_MODEL_NAME: str = "xray_model:latest"

BENTOML_SERVICE_NAME: str = "xray_service"

BENTOML_ECR_URI: str = "xray"

PREDICTION_LABEL: dict = {"0": CLASS_LABEL_1, 1: CLASS_LABEL_2}






