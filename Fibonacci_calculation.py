# Функція caching_fibonacci створює кеш для зберігання результатів обчислень
def caching_fibonacci():
    cache = {} # Словник

        # Внутрішня функція fibonacci. Обчислює число Фібоначчі
    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0. Це базовий випадок
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1. Другий базовий випадок - перше число Фібоначчі
        elif n == 1:
            return 1
        # Якщо результат для n вже є в кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Якщо результату в кеші немає, обчислюємо його рекурсивно і зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Активує функцію та створює замикання ("пам'ятає" стан cache між різними викликами.)
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
