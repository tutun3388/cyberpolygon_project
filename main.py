import os

DATABASE_FILE = "database.txt"


def load_database():
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def save_database(database):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        for record in database:
            file.write(record + "\n")


def show_records(database):
    if not database:
        print("Записей нет.")
    else:
        for i, record in enumerate(database, 1):
            print(f"{i}. {record}")


def add_record(database):
    record = input("Введите новую запись: ")
    database.append(record)
    save_database(database)
    print("Запись добавлена.")


def edit_record(database):
    show_records(database)
    try:
        record_num = int(input("Введите номер записи для редактирования: ")) - 1
        if 0 <= record_num < len(database):
            new_record = input("Введите новый текст записи: ")
            database[record_num] = new_record
            save_database(database)
            print("Запись изменена.")
        else:
            print("Неверный номер записи.")
    except ValueError:
        print("Введите корректный номер.")


def delete_record(database):
    show_records(database)
    try:
        record_num = int(input("Введите номер записи для удаления: ")) - 1
        if 0 <= record_num < len(database):
            deleted_record = database.pop(record_num)
            save_database(database)
            print(f"Запись '{deleted_record}' удалена.")
        else:
            print("Неверный номер записи.")
    except ValueError:
        print("Введите корректный номер.")


def main():
    database = load_database()
    while True:
        print("\n1. Показать записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_records(database)
        elif choice == "2":
            add_record(database)
        elif choice == "3":
            edit_record(database)
        elif choice == "4":
            delete_record(database)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()