import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads yaml file and return
    
    Args:
        path_to_yaml (str): path like input
        
    Raises:
        valueerror: if yaml file is empty
        e: empty file 
        
    returns:
        ConfigBox: ConfigBox type"""
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults"""
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory created: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data 
    Args
        path (path):path to json file
        data (dict): data to be saved in json file
        """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """ load json files data
    
    Args:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

def save_bin(data: Any, path:Path):
    """ save binary file
    
    Args:
        data (any): data to be saved as binary
        path (path): path to binary file 
        """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


def load_bin(path:Path) -> Any:
    """ load binary data

    Args:
        path(path): path to binary file
        
    returns:
        Any: object stored in the file"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
