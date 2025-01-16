# Реалізація стеку на основі масиву для аналізу успішності студентів
# Реалізація стеку на основі масиву для аналізу успішності студентів
class StackArray:
    def __init__(self):
        self.stack = []  # Ініціалізація порожнього списку для зберігання елементів стеку
    
    def push(self, item):
        self.stack.append(item)  # Додавання елемента до вершини стеку
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Видалення і повернення елемента з вершини стеку
        return None  # Якщо стек порожній, повертається None
    
    def is_empty(self):
        return len(self.stack) == 0  # Перевірка, чи є стек порожнім
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Повернення верхнього елемента без видалення
        return None  # Якщо стек порожній, повертається None
    
    def size(self):
        return len(self.stack)  # Повернення кількості елементів у стеку

# Функція для аналізу динаміки успішності за три роки
# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_stack(data):
    stack = StackArray()  # Ініціалізація основного стеку
    
    # Додаємо всі дані у стек
    for year_data in data:
        stack.push(year_data)
    
    temp_stack = StackArray()  # Тимчасовий стек для зберігання витягнутих елементів
    results = []  # Список для збереження результатів аналізу
    
    # Аналізуємо дані, поки у стеку є хоча б три роки
    while stack.size() >= 3:
        # Витягуємо три останні роки зі стеку
        year3 = stack.pop()
        year2 = stack.pop()
        year1 = stack.pop()
        
        # Розрахунок середніх оцінок для кожного року
        avg1 = sum(year1[1]) / len(year1[1])
        avg2 = sum(year2[1]) / len(year2[1])
        avg3 = sum(year3[1]) / len(year3[1])
        
        # Додаємо результат у список результатів
        results.append(f"{year1[0]}-{year3[0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
        
        # Повертаємо три роки назад у тимчасовий стек для наступного аналізу
        temp_stack.push(year1)
        temp_stack.push(year2)
        temp_stack.push(year3)
        
        stack.pop()  # Зсуваємо аналіз на 1 рік назад
    
    # Повертаємо всі дані назад у основний стек
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return results  # Повертаємо список результатів аналізу


# Демонстрація роботи
# Вхідні дані: рік і відповідні оцінки студентів
data = [
    (2020, [85, 90, 78]),
    (2021, [88, 76, 92]),
    (2022, [91, 82, 79]),
    (2023, [93, 85, 88]),
    (2024, [89, 87, 90])
]
    
# Виклик функції аналізу динаміки
trends = analyze_trends_with_stack(data)
    
# Виведення результатів аналізу
print("Динаміка успішності студентів:")
for trend in trends:
    print(trend)
