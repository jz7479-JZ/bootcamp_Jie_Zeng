# src/utils.py
from __future__ import annotations
import os
from pathlib import Path
from typing import Optional, Union

import numpy as np
import pandas as pd

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

def get_project_root(fallback: Optional[Path] = None) -> Path:
    try:
        return Path(__file__).resolve().parents[1]
    except NameError:
        return (fallback or Path.cwd()).resolve()
    
PROJECT_ROOT: Path = get_project_root()
DATA_DIR: Path = Path(os.getenv("DATA_PATH", str(PROJECT_ROOT / "data"))).resolve()
