from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, который записывает логи работы функции"""

    def my_decorator(func: Any) -> Any:
        def wrapper(*args: int, **kwargs: int) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"Function started\nFunction finished\n{func.__name__} ok, result {result}\n")
                else:
                    print(f"Function started\nFunction finished\n{func.__name__} ok, result {result}\n")
            except Exception as error:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(
                            f"Function started\nFunction finished\n{func.__name__} error: {error}. Inputs: {args, kwargs}\n"
                        )
                else:
                    print(
                        f"Function started\nFunction finished\n{func.__name__} error: {error}. Inputs: {args, kwargs}\n"
                    )
                raise error

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
# @log()
def my_function(x: int, y: int) -> Any:
    return x + y


my_function(1, 2)
