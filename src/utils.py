# utils.py - Corrected version
import os
import sys
import pickle  # Explicit import
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)  # Now properly imported
            
    except Exception as e:
        raise CustomException(e, sys)