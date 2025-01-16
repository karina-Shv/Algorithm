# Реалізація двозв'язного списку на основі покажчиків для аналізу успішності студентів
class DoublyNode:
    def __init__(self, year, results):
        self.year = year
        self.results = results
        self.prev = None
        self.next = None

class DoublyLinkedListPointer:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, year, results):
        new_node = DoublyNode(year, results)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_dll_pointer(data):
    dll_pointer = DoublyLinkedListPointer()
    for year_data in data:
        dll_pointer.append(year_data[0], year_data[1])
    
    results = []
    current = dll_pointer.head
    while current and current.next and current.next.next:
        year1, scores1 = current.year, current.results
        year2, scores2 = current.next.year, current.next.results
        year3, scores3 = current.next.next.year, current.next.next.results
        
        # Розрахунок середніх балів
        avg1 = sum(scores1) / len(scores1)
        avg2 = sum(scores2) / len(scores2)
        avg3 = sum(scores3) / len(scores3)
        
        results.append(f"{year1}-{year3}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
        
        current = current.next
    
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
    
    trends = analyze_trends_with_dll_pointer(data)
    print("Динаміка успішності студентів:")
    for trend in trends:
        print(trend)
