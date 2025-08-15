import sys, os
import numpy as np
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

def load_env(path):
    load_dotenv(dotenv_path=path)

def get_key(key):
    value = os.getenv(key)
    if value is None:
        raise KeyError(f"Environment variable '{key}' not found.")
    return value