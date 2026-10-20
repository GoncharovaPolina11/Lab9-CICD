class Calculator:

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")

        return a / b

    def is_prime_number(self, number):
        if number < 2:
            return False

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False

        return True