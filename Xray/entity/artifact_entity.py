from dataclasses import dataclass
from torch.utils.data import DataLoader

@dataclass
class DataIngestionArtifact:
    train_data_path: str
    test_data_path: str
    
    
@dataclass
class DataTransformationArtifact:
    transformed_train_object: DataLoader
    transformed_test_object: DataLoader
    train_transform_file_path: str
    test_transform_file_path: str
    
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    

@dataclass
class ModelEvaluationArtifact:
    model_accuracy: float


@dataclass
class ModelPusherArtifact:
    bentoml_model_name: str

    bentoml_service_name: str
