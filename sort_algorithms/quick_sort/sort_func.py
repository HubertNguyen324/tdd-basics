def sort_array(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]

    return sort_array(left) + middle + sort_array(right)
