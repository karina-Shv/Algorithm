import random

def lsd_radix_sort(numbers):
    # Знаходимо максимальне число, щоб визначити кількість розрядів
    max_number = max(numbers)
    max_digits = len(str(max_number))

    # Виконуємо сортування по кожному розряду з молодшого до старшого
    for digit in range(max_digits):
        buckets = [[] for _ in range(10)]  # 10 кошиків (для цифр 0-9)
        
        for number in numbers:
            # Отримуємо цифру поточного розряду
            digit_value = (number // (10 ** digit)) % 10
            buckets[digit_value].append(number)

        # Об'єднуємо числа з кошиків
        numbers = [number for bucket in buckets for number in bucket]

    return numbers

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

    # Сортуємо список за допомогою LSD сортування
    sorted_fleets = lsd_radix_sort(fleets)
    print("\nВпорядкований список кількості матросів у флотиліях:")
    print(sorted_fleets)
