import time
import random

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір середнього елемента як опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_optimized(arr):
    if len(arr) <= 10:  # Якщо список невеликий, використовуємо сортування вставками
        return insertion_sort(arr)
    first = arr[1]
    second = arr[len(arr) // 2]
    last = arr[-1]
    mean = (first+second+last)/3   
    left = [x for x in arr if x < mean]
    right = [x for x in arr if x > mean]
    return quick_sort_optimized(left) + quick_sort_optimized(right)

# Сортування вставками для малих підмасивів
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def three_way_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір опорного елемента
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return three_way_quick_sort(left) + middle + three_way_quick_sort(right)


# Приклад використання
start_time = time.time()    
ships = [random.randint(0, 50) for i in range(500)]
'''
sorted_ships = quick_sort(ships)
print("Список кораблів після сортування (Quick Sort):", sorted_ships)'''



new_ships = [random.randint(0, 50) for i in range(10)]  # Додані елементи
'''updated_list = ships + new_ships
sorted_updated_list = quick_sort_optimized(updated_list)
print("Список кораблів після оновлення (Modified Quick Sort):", sorted_updated_list)
'''


sorted_ships = three_way_quick_sort(ships)
print("Список кораблів після остаточного сортування (Three-Way Quick Sort):", sorted_ships)

end_time = time.time()
# Вимірювання часу
duration = end_time - start_time
duration_ms = duration * 1000
print(f"Время выполнения: {duration_ms:.5f} миллисекунд")