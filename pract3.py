# Клас StackArray реалізує структуру даних "Стек" на основі масиву (списку)
class StackArray:
    def __init__(self):
        # Ініціалізація порожнього стеку
        self.stack = []
    
    def push(self, item):
        # Додає елемент на вершину стеку
        self.stack.append(item)
    
    def pop(self):
        # Видаляє та повертає елемент із вершини стеку, якщо стек не порожній
        if not self.is_empty():
            return self.stack.pop()
        return None  # Якщо стек порожній, повертає None
    
    def is_empty(self):
        # Перевіряє, чи є стек порожнім
        return len(self.stack) == 0
    
    def peek(self):
        # Повертає елемент на вершині стеку без видалення
        if not self.is_empty():
            return self.stack[-1]
        return None  # Якщо стек порожній, повертає None
    
    def size(self):
        # Повертає кількість елементів у стеку
        return len(self.stack)


# Клас DoublyLinkedListArray реалізує двозв’язний список на основі масиву (списку)
class DoublyLinkedListArray:
    def __init__(self):
        # Ініціалізація порожнього списку для зберігання пар (рік, список оцінок)
        self.data = []
    
    def append(self, year, results):
        # Додає новий запис із роком і відповідним списком оцінок до списку
        self.data.append((year, results))
    
    def analyze_trends(self):
        # Аналізує динаміку успішності за три послідовні роки
        for i in range(len(self.data) - 2):
            # Обчислення середнього бала для кожного з трьох років
            avg1 = sum(self.data[i][1]) / len(self.data[i][1])
            avg2 = sum(self.data[i+1][1]) / len(self.data[i+1][1])
            avg3 = sum(self.data[i+2][1]) / len(self.data[i+2][1])
            
            # Виведення динаміки середніх балів за три роки
            print(f"{self.data[i][0]}-{self.data[i+2][0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")


# Демонстрація роботи стеку на основі масиву
print("Стек на основі масиву:")
stack_array = StackArray()  # Створення об'єкта стеку

# Додавання списків оцінок у стек
stack_array.push([85, 90, 78])
stack_array.push([88, 76, 92])
stack_array.push([91, 82, 79])

# Виведення елементів зі стеку у зворотному порядку їх додавання
while not stack_array.is_empty():
    print(stack_array.pop())


# Демонстрація роботи аналізу динаміки успішності
print("\nДинаміка успішності (масив):")
performance_array = DoublyLinkedListArray()  # Створення об'єкта двозв’язного списку

# Додавання даних про оцінки студентів за різні роки
performance_array.append(2020, [85, 90, 78])
performance_array.append(2021, [88, 76, 92])
performance_array.append(2022, [91, 82, 79])
performance_array.append(2023, [93, 85, 88])
performance_array.append(2024, [89, 87, 90])

# Аналіз та виведення динаміки змін середніх оцінок за три послідовні роки
performance_array.analyze_trends()
