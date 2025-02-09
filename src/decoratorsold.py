from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, который записывает логи работы функции"""

    def my_decorator(func: Any) -> Any:
        def wrapper(*args: int, **kwargs: int) -> Any:
            if filename:
                try:
                    result = func(*args, **kwargs)
                    log_message = f"{func.__name__} ok, result {result}\n"
                except Exception as error:
                    result = "Error"
                    log_message = f"{func.__name__} error: {error}. Inputs: {args, kwargs}\n"
                with open(filename, "a") as file:
                    file.write("Function started\n")
                    file.write("Function finished\n")
                    file.write(log_message)
            else:
                try:
                    print("Function started\n")
                    result = func(*args, **kwargs)
                    print("Function finished\n")
                    log_message = f"{func.__name__} ok, result {result}\n"
                    print(log_message)
                except Exception as error:
                    print("Function finished\n")
                    result = "Error"
                    log_message = f"{func.__name__} error: {error}. Inputs: {args, kwargs}\n"
                    print(log_message)
                    raise error
            return result

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
#@log()
def my_function1(x: int, y: int) -> Any:
    return x + y


my_function1(1, 4)
