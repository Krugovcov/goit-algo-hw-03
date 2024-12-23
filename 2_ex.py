import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000):
        return []
    if(quantity > max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
numbers = get_numbers_ticket(1, 5, 2)
print(numbers)