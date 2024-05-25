import functools

# Декоратор для логирования вызовов функции
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Декоратор для кэширования вызовов функции
def cache_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(sorted(kwargs.items()))
        if cache_key in wrapper.cache:
            print(f"{func.__name__} cache hit")
            return wrapper.cache[cache_key]
        else:
            print(f"{func.__name__} cache miss")
            result = func(*args, **kwargs)
            wrapper.cache[cache_key] = result
            return result
    wrapper.cache = {}
    return wrapper

# Функция, которую необходимо декорировать
@log_calls
@cache_calls
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования
if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(10))