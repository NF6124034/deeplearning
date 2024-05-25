from datetime import datetime
from typing import List

import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

####################################

ARTIFACT_DIR: str = "artifact"

BUCKET_NAME: str = "testing0524"

S3_DATA_FOLDER: str = "test"

CLASS_LABEL_1: str="NORMAL"

CLASS_LABEL_2: str="PNEUMONIA"

