from typing import List, Dict

def sort_by_date(operations: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует операции по дате.
    :param operations: Список операций (каждая операция — словарь с ключом 'date').
    :param reverse: Если True — сортировка по убыванию (сначала новые).
    :return: Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse)