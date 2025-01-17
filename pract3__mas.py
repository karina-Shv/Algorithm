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

    def analyze_year_with_neighbors(self, year):
         # Перевірка коректності введеного року
        if not isinstance(year, int):
            print("Помилка: Введіть коректний рік у числовому форматі.")
            return

        years_in_data = [item[0] for item in self.data]
        if year not in years_in_data:
            print(f"Рік {year} відсутній у даних.")
            return
        # Аналіз обраного року з двома сусідніми
        for i in range(1, len(self.data) - 1):
            if self.data[i][0] == year:
                # Отримання трьох послідовних років
                prev_year, prev_scores = self.data[i - 1]
                curr_year, curr_scores = self.data[i]
                next_year, next_scores = self.data[i + 1]

                # Обчислення середніх балів
                avg_prev = sum(prev_scores) / len(prev_scores)
                avg_curr = sum(curr_scores) / len(curr_scores)
                avg_next = sum(next_scores) / len(next_scores)

                # Виведення результату
                print(f"Аналіз {prev_year}-{next_year}: {avg_prev:.2f} -> {avg_curr:.2f} -> {avg_next:.2f}")
                return
        
        print(f"Неможливо виконати аналіз для {year}. Переконайтеся, що є сусідні роки для аналізу.")




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

# Аналіз обраного року з сусідніми
print("\nАналіз обраного року (2021):")
performance_array.analyze_year_with_neighbors(2021)

print("\nАналіз обраного року (2023):")
performance_array.analyze_year_with_neighbors(2023)

print("\nСпроба аналізу для 2019 року (немає попереднього):")
performance_array.analyze_year_with_neighbors(2019)

print("\nСпроба аналізу для 2021 року (немає такого року):")
performance_array.analyze_year_with_neighbors(2021)
