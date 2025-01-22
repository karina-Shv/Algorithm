import time
import random

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Знайти мінімальний елемент у невідсортованій частині
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Обміняти місцями мінімальний елемент з поточним
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # Взяти поточний елемент
        key = arr[i]
        j = i - 1
        # Перемістити елементи, які більші за key, на одну позицію вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставити поточний елемент у правильну позицію
        arr[j + 1] = key
    return arr

def counting_sort(arr, max_value):
    # Ініціалізуємо список для підрахунку
    count = [0] * (max_value + 1)
    # Підрахунок кількості кожного елемента
    for num in arr:
        count[num] += 1
    
    # Формуємо впорядкований список
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr


start_time = time.time()   

''' 
#Сортування вибором
ships = [random.randint(0, 50) for i in range(1000)]
print(ships)
sorted_ships = selection_sort(ships)
print("Список кораблів після сортування (Selection Sort):", sorted_ships)

#Сортування вставками
ships = [random.randint(0, 50) for i in range(200)]
new_ships = [random.randint(0, 50) for i in range(10)]
updated_list = ships + new_ships
sorted_updated_list = insertion_sort(updated_list)
print("Список кораблів після оновлення (Insertion Sort):", sorted_updated_list)
'''
#Сортування підрахунком
ships = [random.randint(0, 50) for i in range(100)]
print(ships)
max_sailors = max(ships)  # Максимальна кількість матросів
print(max_sailors)
sorted_ships = counting_sort(ships, max_sailors)
print("Список кораблів після остаточного сортування (Counting Sort):", sorted_ships)

end_time = time.time()
duration = end_time - start_time
duration_ms = duration * 1000
print(f"Время выполнения: {duration_ms:.5f} миллисекунд")

'''
# Вимірювання часу
data = [random.randint(0, 100) for i in range(10)]
sorted_data = selection_sort(data)
print(f"Список кораблів після сортування (Selection Sort): {measure_time(sorted_data, arr):.6f}s)")

data2 = [random.randint(0, 100) for i in range(10)]
sorted_data2 = insertion_sort(data2)
print(f"Список кораблів після оновлення (Insertion Sort): {measure_time(sorted_data2, arr):.6f}")
data3 = [random.randint(0, 100) for i in range(10)]
sorted_data3 = counting_sort(data3)
print(f"Список кораблів після остаточного сортування (Counting Sort):", sorted_data3)'''