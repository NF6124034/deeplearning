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
