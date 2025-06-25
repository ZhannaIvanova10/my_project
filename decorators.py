import functools
from typing import Callable, Any, Optional
from datetime import datetime


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Опциональный путь к файлу для записи логов.
                 Если не указан, логи выводятся в консоль.

    Returns:
        Декорированную функцию с логированием.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                log_message = f"{timestamp} - {func_name} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                return result
            except Exception as e:
                error_message = f"{timestamp} - {func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")

                raise

        return wrapper

    return decorator
