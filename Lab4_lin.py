import random
from datetime import datetime, timedelta

class LinearProbingHashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        # Преобразование строки (даты) в числовой хеш
        date_obj = datetime.strptime(key, "%Y-%m-%d")
        return date_obj.toordinal() % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None

    def display(self):
        for i, entry in enumerate(self.table):
            if entry is not None:
                print(f"Index {i}: Key = {entry[0]}, Value = {entry[1]}")
            else:
                print(f"Index {i}: None")

def generate_birthdates(n):
    birthdates = []
    start_date = datetime(1995, 1, 1)
    end_date = datetime(2005, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for _ in range(n):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        birthdates.append(random_date.strftime("%Y-%m-%d"))

    return birthdates

# Основна частина програми
if __name__ == "__main__":
    # Кількість хлопців у потоці
    num_students = 20

    # Генеруємо список дат народження
    birthdates = generate_birthdates(num_students)
    print("Список дат народження:")
    print(birthdates)

    # Створюємо хеш-таблицю
    hash_table = LinearProbingHashTable(size=50)

    # Заповнюємо хеш-таблицю
    for i, birthdate in enumerate(birthdates):
        hash_table.insert(birthdate, f"Student {i + 1}")

    # Виводимо хеш-таблицю
    print("\nХеш-таблиця:")
    hash_table.display()

    # Перевірка пошуку
    test_date = birthdates[0]
    print(f"\nПошук студента з датою народження {test_date}:")
    result = hash_table.search(test_date)
    if result:
        print(f"Знайдено: {result}")
    else:
        print("Дату не знайдено в хеш-таблиці.")
