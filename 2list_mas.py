# Реалізація двозв'язного списку на основі масиву для аналізу успішності студентів
class DoublyLinkedListArray:
    def __init__(self):
        self.data = []
    
    def append(self, year, results):
        self.data.append((year, results))
    
    def size(self):
        return len(self.data)
    
    def get(self, index):
        if 0 <= index < self.size():
            return self.data[index]
        return None

# Функція для аналізу динаміки успішності за три роки
def analyze_trends_with_dll_array(data):
    dll_array = DoublyLinkedListArray()
    for year_data in data:
        dll_array.append(year_data[0], year_data[1])
    
    results = []
    for i in range(dll_array.size() - 2):
        year1, scores1 = dll_array.get(i)
        year2, scores2 = dll_array.get(i + 1)
        year3, scores3 = dll_array.get(i + 2)
        
        # Розрахунок середніх балів
        avg1 = sum(scores1) / len(scores1)
        avg2 = sum(scores2) / len(scores2)
        avg3 = sum(scores3) / len(scores3)
        
        results.append(f"{year1}-{year3}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
    
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
    
    trends = analyze_trends_with_dll_array(data)
    print("Динаміка успішності студентів:")
    for trend in trends:
        print(trend)