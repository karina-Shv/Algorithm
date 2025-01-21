# Клас вузла двозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data      # Значення вузла
        self.prev = None      # Посилання на попередній вузол
        self.next = None      # Посилання на наступний вузол

# Клас двозв'язного списку
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Посилання на перший елемент списку
        self.tail = None      # Посилання на останній елемент списку

    # Метод для додавання елемента в кінець списку
    def add(self, data):
        new_node = Node(data)  # Створення нового вузла
        if self.head is None:  # Якщо список порожній
            self.head = self.tail = new_node  # Новий вузол стає першим і останнім
        else:
            self.tail.next = new_node  # Поточний останній вузол вказує на новий
            new_node.prev = self.tail  # Новий вузол вказує на попередній
            self.tail = new_node      # Оновлення tail на новий вузол

    # Метод для видалення елемента за значенням
    def remove(self, data):
        current = self.head  # Початок пошуку з голови списку
        while current is not None:
            if current.data == data:  # Якщо знайдено елемент для видалення
                if current.prev is not None:
                    current.prev.next = current.next  # Пропускаємо поточний вузол
                else:
                    self.head = current.next  # Видаляємо головний елемент

                if current.next is not None:
                    current.next.prev = current.prev  # Оновлення посилання назад
                else:
                    self.tail = current.prev  # Видаляємо останній елемент
                return  # Завершення після видалення
            current = current.next  # Перехід до наступного вузла
        print("Element not found")  # Якщо елемент не знайдено

    # Метод для виведення елементів списку
    def display(self):
        current = self.head  # Початок з голови списку
        result = []
        while current is not None:
            result.append(current.data)  # Додавання значення у список результатів
            current = current.next  # Перехід до наступного вузла
        print("List:", result)  # Виведення списку

# Приклад використання
dll = DoublyLinkedList()
dll.add(10)  # Додаємо елемент 10
dll.add(20)  # Додаємо елемент 20
dll.add(30)  # Додаємо елемент 30
dll.display()  # Виводимо список

dll.remove(20)  # Видаляємо елемент 20
dll.display()   # Виводимо список після видалення

dll.add(40)  # Додаємо елемент 40
dll.display()  # Виводимо оновлений список
