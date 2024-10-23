# Декоратор для обробки помилок введення
def input_error(func):
    """
    Декоратор для обробки винятків KeyError, ValueError та IndexError.
    
    Параметри:
    func (function): Функція, яку необхідно обгорнути.

    Повертає:
    function: Функція з обробкою помилок.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please, separated by a space"
        except IndexError:
            return "Enter user name."
    return inner

# Функція для розбору введених користувачем команд
def parse_input(user_input):
    """
    Розбирає вхідний рядок на команду і аргументи.
    
    Параметри:
    user_input (str): Рядок введений користувачем.

    Повертає:
    tuple: Команда та аргументи (якщо є).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Переводить команду в нижній регістр і видаляє зайві пробіли
    return cmd, *args

@input_error
# Функція для додавання контакту у словник
def add_contact(args, contacts):
    """
    Додає новий контакт до словника.

    Параметри:
    args (list): Ім'я та номер телефону.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Повідомлення про успішне додавання або помилку.
    """
    if len(args) != 2:
        raise ValueError
    name, phone = args  # Отримуємо ім'я та телефон з аргументів
    contacts[name] = phone  # Додаємо контакт до словника
    return "Contact added."

@input_error
# Функція для зміни номера телефону існуючого контакту
def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.

    Параметри:
    args (list): Ім'я та новий номер телефону.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Повідомлення про успішне оновлення або помилку.
    """
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone  # Оновлюємо номер телефону
        return f"Contact {name} updated."
    else:
        raise KeyError

@input_error
# Функція для виведення номера телефону за іменем
def get_phone(args, contacts):
    """
    Виводить номер телефону для зазначеного контакту.

    Параметри:
    args (list): Ім'я контакту.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Номер телефону або повідомлення про відсутність контакту.
    """
    if len(args) == 0:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        raise KeyError
    
@input_error
# Функція для видалення контакту з словника
def del_contact(args, contacts):
    """
    Видаляє контакт зі словника

    Параметри:
    args (list): Ім'я контакту.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Повідомлення про успішне видалення або помилку.
    """
    if len(args) == 0:
        raise IndexError
    name = args[0]
    if name in contacts:
        del contacts[name] # Видаляємо контакт зі словника
        return f"Contact {name} deleted"
    else:
        raise KeyError

@input_error
# Функція для виведення всіх контактів
def show_all_contacts(contacts):
    """
    Виводить усі збережені контакти.

    Параметри:
    contacts (dict): Словник з контактами.

    Повертає:
    str: Список усіх контактів або повідомлення про порожню записну книжку.
    """
    if contacts:
        all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"All contacts:\n{all_contacts}"
    else:
        return "No contacts found."

# Основна функція
def main():
    """
    Основна функція програми. Відповідає за взаємодію з користувачем і обробку команд.
    """
    contacts = {}  # Ініціалізація словника для контактів
    print("Welcome to the assistant bot!")  # Вітання користувача
    while True:
        user_input = input("Enter a command: ")
        # Перевірка на порожнє введення
        if not user_input:
            print("Please enter a command." )
            continue
        command, *args = parse_input(user_input)  # Обробка введеної команди

        if command in ["close", "exit"]:
            print("Good bye!")  # Повідомлення перед завершенням
            break
        elif command == "hello":
            print("How can I help you?")  # Відповідь на команду hello
        elif command == "add":
            print(add_contact(args, contacts))  # Додає новий контакт
        elif command == "change":
            print(change_contact(args, contacts))  # Змінює існуючий контакт
        elif command == "delete":
            print(del_contact(args, contacts))  # Видаляє контакт
        elif command == "phone":
            print(get_phone(args, contacts))  # Виводить номер телефону
        elif command == "all":
            print(show_all_contacts(contacts))  # Виводить усі контакти
        else:
            print("Invalid command.")  # Повідомлення про некоректну команду

if __name__ == "__main__":
    main()  # Запуск основної функції
