# Реалізація стеку на основі покажчиків для аналізу успішності студентів
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.next
            return data
        return None
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        return None
    
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_stack(data):
    stack = StackLinkedList()
    for year_data in data:
        stack.push(year_data)
    
    temp_stack = StackLinkedList()
    results = []
    while stack.size() >= 3:
        # Витягуємо три останні роки
        year3 = stack.pop()
        year2 = stack.pop()
        year1 = stack.pop()
        
        # Розрахунок середніх балів
        avg1 = sum(year1[1]) / len(year1[1])
        avg2 = sum(year2[1]) / len(year2[1])
        avg3 = sum(year3[1]) / len(year3[1])
        results.append(f"{year1[0]}-{year3[0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
        
        # Повертаємо дані назад у стек для наступного аналізу
        temp_stack.push(year1)
        temp_stack.push(year2)
        temp_stack.push(year3)
        
        stack.pop()  # Зсуваємо на 1 рік для наступного аналізу
    
    # Повертаємо всі дані назад у основний стек
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return results

# Демонстрація роботи
if __name__ == "__main__":
    data = [
        (2020, [85, 90, 78]),
        (2021, [88, 76, 92]),
        (2022, [91, 82, 79]),
        (2023, [93, 85, 88]),
        (2024, [89, 87, 90])
    ]
    
    trends = analyze_trends_with_stack(data)
    print("Динаміка успішності студентів:")
    for trend in trends:
        print(trend)