import os
import sys
from Xray.exception import XRayException
from pathlib import Path


class S3Operation:
    def sync_folder_to_s3(self,folder: str, bucket_name: str,bucket_folder_name: str) -> None:
        try:
            command: str = str(Path(f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"))
            
            os.system(command)
        except Exception as e:
            raise XRayException(e, sys)
        
    def sync_folder_from_s3(self,folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        try:
            command: str = f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}"
            print(command)
            
            os.system(command)
            
        except Exception as e:
            raise XRayException(e, sys)
        
