import os
import urllib.request as request
import zipfile
from ml_project import logger   
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,
                 config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_url,
                                filename=self.config.local_data_file)
            logger.info(f"File {filename} downloaded ok with hearders: \n  {headers}")
        else:
            logger.info(f"File already exists : {get_size(self.config.local_data_file)}")
            
    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        