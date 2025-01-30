import random

def bucket_sort(numbers):
    # Створюємо кошики
    max_value = max(numbers)
    size = max_value / len(numbers)

    buckets = [[] for _ in range(len(numbers))]

    # Розподіляємо числа по кошиках
    for number in numbers:
        index = int(number / size)
        if index != len(numbers):
            buckets[index].append(number)
        else:
            buckets[len(numbers) - 1].append(number)

    # Сортуємо кожен кошик окремо
    for bucket in buckets:
        bucket.sort()

    # Об'єднуємо кошики в один впорядкований список
    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers.extend(bucket)

    return sorted_numbers

def generate_random_fleets(num_fleets, min_sailors, max_sailors):
    # Генеруємо випадкові кількості матросів для флотилій
    return [random.randint(min_sailors, max_sailors) for _ in range(num_fleets)]

# Основна частина програми
if __name__ == "__main__":
    # Генеруємо випадковий список кількості матросів для флотилій
    num_fleets = 20  # Кількість флотилій
    min_sailors = 1000  # Мінімальна кількість матросів
    max_sailors = 100000  # Максимальна кількість матросів

    fleets = generate_random_fleets(num_fleets, min_sailors, max_sailors)
    print("Початковий список кількості матросів у флотиліях:")
    print(fleets)

    # Сортуємо список за допомогою сортування кошиком
    sorted_fleets = bucket_sort(fleets)
    print("\nВпорядкований список кількості матросів у флотиліях:")
    print(sorted_fleets)
