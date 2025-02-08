from typing import Any

def log (filename: str) -> Any:
    """Декоратор, который записывает логи работы функции"""
    def my_decorator(func: Any) -> Any:
        def wrapper(*args: int, **kwargs: int) -> int:
            if filename:
                try:
                    result = func(*args, **kwargs)
                    log_message = f"My function ok, result {result}\n"
                except Exception as e:
                    result = "Error"
                    log_message = f"My function error: {e}. Inputs: {args, kwargs}\n"
                with open(filename, "a") as file:
                    file.write("Function started\n")
                    file.write("Function finished\n")
                    file.write(log_message)
            else:
                try:
                    print("Function started\n")
                    result = func(*args, **kwargs)
                    print("Function finished\n")
                    log_message = f"my function ok, result {result}\n"
                    print (log_message)
                except Exception as e:
                    print("Function finished\n")
                    result = "Error"
                    log_message = f"My function error: {e}. Inputs: {args, kwargs}\n"
                    print(log_message)
            return result
        return wrapper
    return my_decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

    