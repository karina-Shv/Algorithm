# Клас вузла двозв'язного списку
class DoublyNode:
    def __init__(self, year, results):
        self.year = year        # Рік, до якого відносяться оцінки
        self.results = results  # Список оцінок студентів за певний рік
        self.prev = None        # Покажчик на попередній елемент списку
        self.next = None        # Покажчик на наступний елемент списку

# Клас для двозв'язного списку на покажчиках
class DoublyLinkedListPointer:
    def __init__(self):
        self.head = None  # Початковий (перший) елемент списку
        self.tail = None  # Кінцевий (останній) елемент списку
    
    def append(self, year, results):
        new_node = DoublyNode(year, results)  # Створення нового вузла
        if not self.head:
            # Якщо список порожній, новий вузол стає першим і останнім
            self.head = self.tail = new_node
        else:
            # Додає новий вузол у кінець списку
            self.tail.next = new_node   # Поточний останній елемент вказує на новий
            new_node.prev = self.tail   # Новий елемент вказує на попередній
            self.tail = new_node        # Оновлюється останній елемент списку

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_dll_pointer(data):
    dll_pointer = DoublyLinkedListPointer()  # Створення списку
    
    # Заповнення списку даними
    for year_data in data:
        dll_pointer.append(year_data[0], year_data[1])
    
    results = []  # Список для збереження результатів аналізу
    
    current = dll_pointer.head  # Починаємо з першого елемента списку
    while current and current.next and current.next.next:
        # Отримуємо дані трьох послідовних років
        year1, scores1 = current.year, current.results
        year2, scores2 = current.next.year, current.next.results
        year3, scores3 = current.next.next.year, current.next.next.results
        
        # Розрахунок середніх балів за кожен рік
        avg1 = sum(scores1) / len(scores1)
        avg2 = sum(scores2) / len(scores2)
        avg3 = sum(scores3) / len(scores3)
        
        # Додаємо результат до списку
        results.append(f"{year1}-{year3}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
        
        current = current.next  # Переходимо до наступного елемента
    
    return results  # Повертаємо результати аналізу

# Демонстрація роботи
# Вхідні дані: рік і список оцінок студентів
data = [
    (2020, [85, 90, 78]),
    (2021, [88, 76, 92]),
    (2022, [91, 82, 79]),
    (2023, [93, 85, 88]),
    (2024, [89, 87, 90])
]
    
# Виклик функції аналізу динаміки
trends = analyze_trends_with_dll_pointer(data)
    
# Виведення результатів аналізу
print("Динаміка успішності студентів:")
for trend in trends:
    print(trend)

