from datetime import datetime

quantity_prime_digits = int(input('Введите желаемое количество простых чисел: '))
start_time = datetime.now()


def check_prime(number):
    for digit in range(2, int(number ** 0.5) + 1):
        if number % digit == 0:
            return False
    return True


def quantity_prime_numbers(prime_quantity):
    quantity = 0
    prime = 2
    while quantity != prime_quantity:
        if check_prime(prime):
            print(prime)
            quantity += 1
        prime += 1


if __name__ == "__main__":
    quantity_prime_numbers(quantity_prime_digits)
    print(f'Время выполнения: {datetime.now() - start_time}')
