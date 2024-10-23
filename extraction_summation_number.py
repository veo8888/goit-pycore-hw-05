import re
from typing import Callable, Generator

# Функція generator_numbers повертає генератор, що ітерує по знайдених числах.
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз для пошуку дійсних чисел у тексті
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    
    # Цикл по знайдених числах
    for num in numbers:
        yield float(num)

# Підсумовує числа з тексту, використовуючи генератор.
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Повертаємо суму чисел
    return sum(func(text))


# Приклад
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# Запуск функцшї sum_profit
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
