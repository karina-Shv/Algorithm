import time
import random
from datetime import datetime, timedelta

class CuckooHashing:
    def __init__(self, size=11):
        self.size = size
        self.table1 = [None] * self.size
        self.table2 = [None] * self.size
        self.max_attempts = 5

    def hash1(self, key):
        date_obj = datetime.strptime(key, "%Y-%m-%d")
        return date_obj.toordinal() % self.size

    def hash2(self, key):
        date_obj = datetime.strptime(key, "%Y-%m-%d")
        return (date_obj.toordinal() // self.size) % self.size

    def rehash(self):
        old_table1 = self.table1
        old_table2 = self.table2
        self.size *= 2
        self.table1 = [None] * self.size
        self.table2 = [None] * self.size
        for key in old_table1 + old_table2:
            if key is not None:
                self.insert(key)

    def insert(self, key):
        start_time = time.time()
        for attempt in range(self.max_attempts):
            pos1 = self.hash1(key)
            if self.table1[pos1] is None:
                self.table1[pos1] = key
                end_time = time.time()
                print(f"Час вставки ключа {key}: {end_time - start_time:.6f} секунд")
                return True

            key, self.table1[pos1] = self.table1[pos1], key

            pos2 = self.hash2(key)
            if self.table2[pos2] is None:
                self.table2[pos2] = key
                end_time = time.time()
                print(f"Час вставки ключа {key}: {end_time - start_time:.6f} секунд")
                return True

            key, self.table2[pos2] = self.table2[pos2], key

        print("Ре-хешування необхідне")
        self.rehash()
        end_time = time.time()
        print(f"Час вставки ключа {key}: {end_time - start_time:.6f} секунд")
        return self.insert(key)

    def search(self, key):
        start_time = time.time()
        pos1 = self.hash1(key)
        if self.table1[pos1] == key:
            end_time = time.time()
            print(f"Час пошуку ключа {key}: {end_time - start_time:.6f} секунд")
            return True

        pos2 = self.hash2(key)
        if self.table2[pos2] == key:
            end_time = time.time()
            print(f"Час пошуку ключа {key}: {end_time - start_time:.6f} секунд")
            return True

        end_time = time.time()
        print(f"Час пошуку ключа {key}: {end_time - start_time:.6f} секунд")
        return False

    def display(self):
        print("Таблиця 1:", self.table1)
        print("Таблиця 2:", self.table2)

def generate_birthdates(n):
    birthdates = []
    start_date = datetime(1980, 1, 1)
    end_date = datetime(2005, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for _ in range(n):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        birthdates.append(random_date.strftime("%Y-%m-%d"))

    return birthdates

cuckoo = CuckooHashing()
birthdates = generate_birthdates(15)

for date in birthdates:
    cuckoo.insert(date)

cuckoo.display()

for date in birthdates:
    found = cuckoo.search(date)
    print(f"Ключ {date} {'знайдено' if found else 'не знайдено'}")
