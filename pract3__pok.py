# Клас Node представляє окремий вузол двозв’язного списку
class Node:
    def __init__(self, year, results):
        self.year = year           # Рік
        self.results = results     # Список оцінок
        self.prev = None           # Посилання на попередній вузол
        self.next = None           # Посилання на наступний вузол

# Клас DoublyLinkedList реалізує двозв’язний список на основі покажчиків
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Початок списку
        self.tail = None  # Кінець списку

    def push(self, year, results):
        """Додає новий вузол до кінця списку"""
        new_node = Node(year, results)
        if self.head is None:
            self.head = self.tail = new_node  # Якщо список порожній
        else:
            self.tail.next = new_node  # Поточний кінець посилається на новий вузол
            new_node.prev = self.tail  # Новий вузол посилається на попередній
            self.tail = new_node       # Новий вузол стає кінцем списку

    def pop(self, year):
        """Видаляє вузол за вказаним роком"""
        current = self.head
        while current:
            if current.year == year:
                if current.prev:
                    current.prev.next = current.next  # Пропускаємо поточний вузол
                else:
                    self.head = current.next  # Якщо видаляємо голову

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Якщо видаляємо кінець

                print(f"Запис за {year} рік видалено: {current.results}")
                return
            current = current.next
        print(f"Запис за {year} рік не знайдено.")

    def analyze_trends(self):
        """Аналізує динаміку успішності за три послідовні роки"""
        if self.head is None or self.head.next is None or self.head.next.next is None:
            print("Недостатньо даних для аналізу (потрібно щонайменше 3 роки).")
            return

        current = self.head
        while current and current.next and current.next.next:
            avg1 = sum(current.results) / len(current.results)
            avg2 = sum(current.next.results) / len(current.next.results)
            avg3 = sum(current.next.next.results) / len(current.next.next.results)

            print(f"{current.year}-{current.next.next.year}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
            current = current.next

    def analyze_year_with_neighbors(self, year):
        """Аналіз обраного року з сусідніми роками"""
        current = self.head
        while current:
            if current.year == year:
                if current.prev and current.next:
                    avg_prev = sum(current.prev.results) / len(current.prev.results)
                    avg_curr = sum(current.results) / len(current.results)
                    avg_next = sum(current.next.results) / len(current.next.results)

                    print(f"Аналіз {current.prev.year}-{current.next.year}: {avg_prev:.2f} -> {avg_curr:.2f} -> {avg_next:.2f}")
                else:
                    print(f"Неможливо виконати аналіз для {year}. Переконайтеся, що є сусідні роки для аналізу.")
                return
            current = current.next
        print(f"Рік {year} відсутній у даних.")

# Демонстрація роботи
print("\nДинаміка успішності (двозв’язний список):")
performance_list = DoublyLinkedList()  # Створення об'єкта двозв’язного списку

# Додавання даних
performance_list.push(2019, [79, 85, 93])
performance_list.push(2020, [85, 90, 78])
performance_list.push(2021, [88, 76, 92])
performance_list.push(2022, [91, 82, 79])
performance_list.push(2023, [93, 85, 88])
performance_list.push(2024, [89, 87, 90])

# Аналіз змін середніх оцінок
performance_list.analyze_trends()

# Видалення запису
print("\nВидалення запису за 2021 рік:")
performance_list.pop(2021)

# Аналіз після видалення
print("\nДинаміка успішності після видалення:")
performance_list.analyze_trends()

#Аналіз обраного року
print("\nАналіз обраного року (2023):")
performance_list.analyze_year_with_neighbors(2023)

print("\nСпроба аналізу для 2019 року (немає попереднього):")
performance_list.analyze_year_with_neighbors(2019)

print("\nСпроба аналізу для 2021 року (вже видалено):")
performance_list.analyze_year_with_neighbors(2021)
