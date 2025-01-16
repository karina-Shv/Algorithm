
def count_zeros(matrix):
    count_zeros = 0
    for row in matrix:
        for element in row:
            if element == 0:
                count_zeros += 1
    return count_zeros

n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []
print("Введіть елементи матриці:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = count_zeros(matrix)
print(f"Кількість нулів у матриці: {result}")
