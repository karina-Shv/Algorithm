import time
n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []
print("Введіть елементи матриці:")
for i in range(n):
    row = list(map(int, input().split())) 
    matrix.append(row) 

start = time.monotonic_ns()
count_zeros = 0
for row in matrix:
    for element in row:
        if element == 0: 
            count_zeros += 1 
finish = time.monotonic_ns()
print(f"Кількість нулів у матриці: {count_zeros}")
print('Время работы в наносекундах: ' + str(finish - start))
