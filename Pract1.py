import random
import os

def manual_input():
    n = int(input("Введіть кількість рядків: "))
    m = int(input("Введіть кількість стовпців: "))
    matrix = []
    print("Введіть елементи матриці:")
    for i in range(n):
        row = list(map(int, input().split())) 
        matrix.append(row) 
    return matrix

def auto_generate(n, m, filename):
    matrix = [[random.randint(0, 50) for i in range(m)] for j in range(n)]
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
    return matrix

def read_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.strip().split())) for line in file]
    return matrix

def count_zeros(matrix):
    count_zeros = 0
    for row in matrix:
        for element in row:
            if element == 0: 
                count_zeros += 1 
    return count_zeros


print("Оберіть спосіб введення даних:")
print("1 - Ручне введення")
print("2 - Автоматична генерація і запис у файл")
print("3 - Зчитування з файлу")
choice = input("Ваш вибір: ")
    
if choice == '1':
    matrix = manual_input()
elif choice == '2':
    n = int(input("Введіть кількість рядків: "))
    m = int(input("Введіть кількість стовпців: "))
    filename = "namesome.txt"
    matrix = auto_generate(n, m, filename)
    print(f"Масив збережено у файл {filename}")
elif choice == '3':
    filename = input("Введіть назву файлу: ")
    if not os.path.exists(filename):
        print("Файл не знайдено.")        
    matrix = read_from_file(filename)
else:
    print("Неправильний вибір.")    
    
result = count_zeros(matrix)
print(f"Кількість нулів у масиві: {result}")



