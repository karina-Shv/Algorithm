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

#Сортування вибором
ships = [45, 32, 67, 12, 89, 34]
print(f"Список кораблів: {ships}")
sorted_ships = selection_sort(ships)
print("Список кораблів після сортування (Selection Sort):", sorted_ships)

#Сортування вставками
new_ships = [12, 34, 45, 12, 67, 89, 34, 45, 12]
updated_list = ships + new_ships
sorted_updated_list = insertion_sort(updated_list)
print("Список кораблів після оновлення (Insertion Sort):", sorted_updated_list)

#Сортування підрахунком
max_sailors = 100  # Максимальна кількість матросів
sorted_ships = counting_sort(ships, max_sailors)
print("Список кораблів після остаточного сортування (Counting Sort):", sorted_ships)


