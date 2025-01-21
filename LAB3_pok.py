class Node:
    def __init__(self, year, scores):
        self.year = year           # Рік
        self.scores = scores       # Список балів за рік
        self.prev = None           # Посилання на попередній вузол
        self.next = None           # Посилання на наступний вузол

class DoublyLinkedList:
    def __init__(self):
        self.head = None           # Посилання на перший елемент списку
        self.tail = None           # Посилання на останній елемент списку

    # Метод для додавання року та балів
    def push(self, year, scores):
        new_node = Node(year, scores)  # Створення нового вузла
        if self.head is None:          # Якщо список порожній
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Метод для видалення року за значенням
    def pop(self, year):
        current = self.head
        while current is not None:
            if current.year == year:  # Якщо знайдено вузол з відповідним роком
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev                
                print(f"Запис за {year} рік видалено.")
                return
            current = current.next
        print(f"Запис за {year} рік не знайдено.")

    # Метод для виведення середніх балів за три послідовні роки
    def analyze(self):
        current = self.head
        while current is not None and current.next is not None and current.next.next is not None:
            year1 = current.year
            year2 = current.next.year
            year3 = current.next.next.year

            # Розрахунок середнього бала для кожного року
            avg1 = sum(current.scores) / len(current.scores)
            avg2 = sum(current.next.scores) / len(current.next.scores)
            avg3 = sum(current.next.next.scores) / len(current.next.next.scores)

            percent = (avg3-avg1)*100/(avg1)
            print(f"{year1}-{year3}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}    ({percent:.2f}%)")
            current = current.next
    # Метод для виведення всього списку
    def display(self):
        current = self.head
        while current is not None:
            print(f"Рік: {current.year}, Бали: {current.scores}")
            current = current.next

# Приклад використання
# Ініціалізація списку
dll = DoublyLinkedList()

# Додавання даних про успішність студентів за роками
dll.push(2019, [70, 75, 80, 95])
dll.push(2020, [78, 82, 88, 59])
dll.push(2021, [84, 86, 89, 99])
dll.push(2022, [79, 85, 83, 75])
dll.push(2023, [88, 90, 92, 100])
dll.push(2024, [85, 80, 90, 32])

# Виведення списку
dll.display()

# Аналіз середніх балів за три підряд роки
dll.analyze()

# Видалення року та повторний аналіз
dll.pop(2021)
dll.display()
dll.analyze()
