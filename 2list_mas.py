# Реалізація двозв'язного списку на основі масиву для аналізу успішності студентів
class DoublyLinkedListArray:
    def __init__(self):
        # Ініціалізація порожнього списку для зберігання пар (рік, оцінки)
        self.data = []
    
    def append(self, year, results):
        # Додає новий елемент у вигляді пари (рік, список оцінок) до списку
        self.data.append((year, results))
    
    def size(self):
        # Повертає кількість елементів у списку
        return len(self.data)
    
    def get(self, index):
        # Повертає елемент за індексом, якщо він у межах списку
        if 0 <= index < self.size():
            return self.data[index]
        return None  # Повертає None, якщо індекс некоректний

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_dll_array(data):
    # Створення об'єкта двозв’язного списку на масиві
    dll_array = DoublyLinkedListArray()
    
    # Додавання даних до списку
    for year_data in data:
        dll_array.append(year_data[0], year_data[1])
    
    results = []  # Список для збереження результатів аналізу
    
    # Проходження по списку для аналізу трьох послідовних років
    for i in range(dll_array.size() - 2):
        # Отримання даних для трьох років поспіль
        year1, scores1 = dll_array.get(i)
        year2, scores2 = dll_array.get(i + 1)
        year3, scores3 = dll_array.get(i + 2)
        
        # Розрахунок середніх оцінок для кожного року
        avg1 = sum(scores1) / len(scores1)
        avg2 = sum(scores2) / len(scores2)
        avg3 = sum(scores3) / len(scores3)
        
        # Додавання результату аналізу до списку
        results.append(f"{year1}-{year3}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
    
    return results  # Повернення результатів аналізу


# Демонстрація роботи
# Вхідні дані: пари (рік, список оцінок студентів)
data = [
    (2019, [79, 85, 93]),
    (2020, [85, 90, 78]),
    (2021, [88, 76, 92]),
    (2022, [91, 82, 79]),
    (2023, [93, 85, 88]),
    (2024, [89, 87, 90])
]
    
# Виклик функції для аналізу динаміки
trends = analyze_trends_with_dll_array(data)
    
# Виведення результатів аналізу
print("Динаміка успішності студентів:")
for trend in trends:
    print(trend)
