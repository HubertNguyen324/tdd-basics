def add(input_str: str) -> int:
    if not input_str:
        return 0

    input_str = input_str.replace("\n", ",")
    input_str = input_str.replace(" ", ",")
    numbers = input_str.split(",")

    return sum(int(num) for num in numbers)
