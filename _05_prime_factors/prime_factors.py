def generate_prime_factors(number: int) -> list[int]:
    if number < 0:
        raise ValueError("Number must be positive")

    if number == 1:
        return []

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return [i] + generate_prime_factors(number // i)
    return [number]
