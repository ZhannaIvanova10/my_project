from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Обрабатывает список словарей с данными"""
    processed = []
    for item in data:
        processed.append({
            'id': item.get('id'),
            'value': item.get('value', 0) * 2
        })
    return processed
