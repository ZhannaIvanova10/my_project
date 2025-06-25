import json
from pathlib import Path
from typing import List, Dict, Any


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Read transactions from JSON file.

    Args:
        file_path: Path to JSON file

    Returns:
        List of transactions or empty list if file is empty, invalid or not found
    """
    try:
        with Path(file_path).open(encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return []
