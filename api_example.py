from typing import Any  # Добавьте этот импорт
import requests

def fetch_json(url: str) -> dict[str, Any]:  # Заменили any на Any
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = fetch_json("https://api.github.com")
    print(data)
