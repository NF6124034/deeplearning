from dataclasses import dataclass
from torch.utils.data import DataLoader

@dataclass
class DataIngestionArtifact:
    train_data_path: str
    test_data_path: str
