# Клас вузла для однозв'язного списку (елемента стеку)
class Node:
    def __init__(self, data):
        self.data = data  # Дані, що зберігаються у вузлі
        self.next = None  # Покажчик на наступний елемент

# Клас стеку на основі однозв'язного списку
class StackLinkedList:
    def __init__(self):
        self.top = None  # Ініціалізація вершини стеку
    
    def push(self, item):
        new_node = Node(item)  # Створення нового вузла
        new_node.next = self.top  # Новий вузол вказує на поточну вершину
        self.top = new_node  # Оновлення вершини стеку
    
    def pop(self):
        if not self.is_empty():
            data = self.top.data  # Зберігаємо дані з вершини
            self.top = self.top.next  # Видаляємо верхній елемент
            return data  # Повертаємо дані
        return None  # Якщо стек порожній, повертаємо None
    
    def is_empty(self):
        return self.top is None  # Перевірка, чи порожній стек
    
    def peek(self):
        if not self.is_empty():
            return self.top.data  # Повернення верхнього елемента без видалення
        return None  # Якщо стек порожній, повертаємо None
    
    def size(self):
        count = 0
        current = self.top  # Починаємо з вершини
        while current:  # Проходимо по всьому стеку
            count += 1
            current = current.next  # Переходимо до наступного елемента
        return count  # Повертаємо кількість елементів у стеку
    
    def to_list(self):
        """Перетворення стеку в список для зручного аналізу."""
        current = self.top
        result = []
        while current:
            result.insert(0, current.data)  # Додаємо елементи в порядку вставки
            current = current.next
        return result

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_stack(data):
    stack = StackLinkedList()  # Ініціалізація основного стеку
    
    # Додаємо всі роки у стек
    for year_data in data:
        stack.push(year_data)
    
    results = []  # Список для збереження результатів аналізу
    data_list = stack.to_list()  # Перетворюємо стек у список для зручності

    # Проходимо по всіх послідовних трійках років
    for i in range(len(data_list) - 2):
        year1 = data_list[i]
        year2 = data_list[i + 1]
        year3 = data_list[i + 2]
        
        # Розрахунок середніх балів для кожного року
        avg1 = sum(year1[1]) / len(year1[1])
        avg2 = sum(year2[1]) / len(year2[1])
        avg3 = sum(year3[1]) / len(year3[1])
        
        # Додаємо результат у список
        results.append(f"{year1[0]}-{year3[0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
    
    return results  # Повертаємо результати аналізу

# Демонстрація роботи програми
# Вхідні дані: рік і відповідні оцінки
data = [
    (2019, [79, 85, 93]),
    (2020, [85, 90, 78]),
    (2021, [88, 76, 92]),
    (2022, [91, 82, 79]),
    (2023, [93, 85, 88]),
    (2024, [89, 87, 90])
]
    
# Аналіз динаміки успішності
trends = analyze_trends_with_stack(data)
    
# Виведення результатів аналізу
print("Динаміка успішності студентів:")
for trend in trends:
    print(trend)
