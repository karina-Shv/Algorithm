 
# Введення кількості рядків матриці від користувача
n = int(input("Введіть кількість рядків: "))
# Введення кількості стовпців матриці від користувача
m = int(input("Введіть кількість стовпців: "))

# Ініціалізація порожнього списку для збереження рядків матриці
matrix = []
# Повідомлення користувачу про необхідність введення елементів матриці
print("Введіть елементи матриці:")
# Цикл для введення кожного рядка матриці
for i in range(n):
    row = list(map(int, input().split())) # Зчитування рядка як списку чисел
    matrix.append(row) # Додавання введеного рядка до матриці

# Ініціалізація змінної для підрахунку кількості нулів у матриці
count_zeros = 0
# Зовнішній цикл для ітерації по кожному рядку матриці
for row in matrix:
# Внутрішній цикл для ітерації по кожному елементу поточного рядка
    for element in row:
        if element == 0: # Перевірка, чи дорівнює поточний елемент нулю
            count_zeros += 1 # Збільшення лічильника нулів на 1, якщо умова виконана
# Виведення результату: загальної кількості нулів у матриці
print(f"Кількість нулів у матриці: {count_zeros}")
