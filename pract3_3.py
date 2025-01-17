# Клас DoublyLinkedListArray реалізує двозв’язний список на основі масиву (списку)
class DoublyLinkedListArray:
    def __init__(self):
        # Ініціалізація порожнього списку для зберігання пар (рік, список оцінок)
        self.data = []
    
    def push(self, year, results):
        # Додає новий запис із роком і відповідним списком оцінок до списку
        self.data.append((year, results))

    def pop(self, year):
        # Видаляє запис за вказаним роком
        for i in range(len(self.data)):
            if self.data[i][0] == year:
                removed_item = self.data.pop(i)
                print(f"Запис за {year} рік видалено: {removed_item[1]}")
                return
        print(f"Запис за {year} рік не знайдено.")
    
    def analyze_trends(self):
        if len(self.data) < 3:
            print("Недостатньо даних для аналізу (потрібно щонайменше 3 роки).")
            return
        # Аналізує динаміку успішності за три послідовні роки
        for i in range(len(self.data) - 2):
            # Обчислення середнього бала для кожного з трьох років
            avg1 = sum(self.data[i][1]) / len(self.data[i][1])
            avg2 = sum(self.data[i+1][1]) / len(self.data[i+1][1])
            avg3 = sum(self.data[i+2][1]) / len(self.data[i+2][1])
            
            # Виведення динаміки середніх балів за три роки
            print(f"{self.data[i][0]}-{self.data[i+2][0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")



# Демонстрація роботи аналізу динаміки успішності
print("\nДинаміка успішності (масив):")
performance_array = DoublyLinkedListArray()  # Створення об'єкта двозв’язного списку

# Додавання даних про оцінки студентів за різні роки
performance_array.push(2019, [79, 85, 93])
performance_array.push(2020, [85, 90, 78])
performance_array.push(2021, [88, 76, 92])
performance_array.push(2022, [91, 82, 79])
performance_array.push(2023, [93, 85, 88])
performance_array.push(2024, [89, 87, 90])



# Аналіз та виведення динаміки змін середніх оцінок за три послідовні роки
performance_array.analyze_trends()

# Демонстрація видалення запису
print("\nВидалення запису за 2021 рік:")
performance_array.pop(2021)

# Повторний аналіз після видалення
print("\nДинаміка успішності після видалення:")
performance_array.analyze_trends()
