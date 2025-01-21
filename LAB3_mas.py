class DoublyLinkedListArray:
    def __init__(self):
        self.data = []  # Масив для зберігання вузлів, кожен вузол - це словник

    def push(self, year, scores):
        node = {
            'year': year,          # Рік
            'scores': scores,      # Бали за рік
            'prev': len(self.data) - 1 if self.data else None,  # Індекс попереднього вузла
            'next': None           # Індекс наступного вузла
        }
        if self.data:
            self.data[-1]['next'] = len(self.data)  # Оновлення посилання "next" у попереднього вузла
        self.data.append(node)

    def pop(self, year):
        for i, node in enumerate(self.data):
            if node['year'] == year:
                # Оновлення посилань "prev" і "next"
                if node['prev'] is not None:
                    self.data[node['prev']]['next'] = node['next']
                if node['next'] is not None:
                    self.data[node['next']]['prev'] = node['prev']
                self.data.pop(i)

                # Оновлення індексів у масиві після видалення
                for j, n in enumerate(self.data):
                    if n['prev'] is not None and n['prev'] > i:
                        n['prev'] -= 1
                    if n['next'] is not None and n['next'] > i:
                        n['next'] -= 1
                print(f"Запис за {year} рік видалено.")
                return
        print(f"Запис за {year} рік не знайдено.")

    def analyze(self):
        if len(self.data) < 3:
            print("Недостатньо даних для аналізу (потрібно щонайменше 3 роки).")
            return

        current_index = 0
        while current_index is not None and self.data[current_index]['next'] is not None:
            next_index = self.data[current_index]['next']
            next_next_index = self.data[next_index]['next'] if next_index is not None else None

            if next_next_index is None:
                break

            # Обчислення середніх балів за три підряд роки
            avg1 = sum(self.data[current_index]['scores']) / len(self.data[current_index]['scores'])
            avg2 = sum(self.data[next_index]['scores']) / len(self.data[next_index]['scores'])
            avg3 = sum(self.data[next_next_index]['scores']) / len(self.data[next_next_index]['scores'])
            percent = (avg3-avg1)*100/(avg1)
            print(f"{self.data[current_index]['year']}-{self.data[next_next_index]['year']}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}    ({percent:.2f}%)")

            current_index = self.data[current_index]['next']

    def display(self):
        for node in self.data:
            print(f"Рік: {node['year']}, Бали: {node['scores']}")



# Приклад використання
dll_array = DoublyLinkedListArray()

# Додавання даних про успішність студентів за роками
dll_array.push(2019, [70, 75, 80, 95])
dll_array.push(2020, [78, 82, 88, 59])
dll_array.push(2021, [84, 86, 89, 99])
dll_array.push(2022, [79, 85, 83, 75])
dll_array.push(2023, [88, 90, 92, 100])
dll_array.push(2024, [85, 80, 90, 32])

dll_array.display()

# Аналіз середніх балів за три підряд роки
dll_array.analyze()

# Видалення року та повторний аналіз
dll_array.pop(2020)
dll_array.display()
dll_array.analyze()
