import random

def get_numbers_ticket(min, max, quantity):
    """
    Функція генерує набір унікальних випадкових чисел для лотерейного білета.

    Параметри:
      min - мінімально допустиме число (не менше 1)
      max - максимально допустиме число (не більше 1000)
      quantity - кількість чисел у списку

    Повертає:
      Відсортований список унікальних чисел,
      або порожній список, якщо параметри некоректні.
    """
    incorrect_number = (max > 1000 or min < 1 or min > max or quantity < 1 or quantity > max - min + 1)
    if incorrect_number:
        return []
    else:
        # random.sample гарантує відсутність повторів
        numbers = random.sample(range(min, max + 1), k=quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)