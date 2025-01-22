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
    pivot = arr[len(arr) // 2]  # Вибір опорного елемента
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_optimized(left) + middle + quick_sort_optimized(right)

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
ships = [45, 32, 67, 12, 89, 34]
print(f"Список кораблів: {ships}")
sorted_ships = quick_sort(ships)
print("Список кораблів після сортування (Quick Sort):", sorted_ships)


new_ships = [32, 38]  # Додані елементи
updated_list = ships + new_ships
sorted_updated_list = quick_sort_optimized(updated_list)
print("Список кораблів після оновлення (Modified Quick Sort):", sorted_updated_list)


sorted_ships = three_way_quick_sort(ships)
print("Список кораблів після остаточного сортування (Three-Way Quick Sort):", sorted_ships)