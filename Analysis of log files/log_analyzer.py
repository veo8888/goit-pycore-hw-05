import sys

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)  # Розбиваємо на 4 частини: дата, час, рівень логування, повідомлення
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message.strip()}

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# Функція для підрахунку кількості записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    levels = {}
    for log in logs:
        level = log['level']
        levels[level] = levels.get(level, 0) + 1
    return levels

# Функція для виводу підрахованих результатів у вигляді таблиці
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<9}")

# Основна функція
def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу як аргумент.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main() # Запуск основної функції
