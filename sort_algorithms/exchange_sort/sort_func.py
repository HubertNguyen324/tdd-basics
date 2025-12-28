def sort_array(arr: list[int]) -> list[int]:
    sorted_arr: list[int] = arr
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if sorted_arr[i] > sorted_arr[j]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
    return sorted_arr
