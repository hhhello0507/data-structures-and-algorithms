def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        center = (left + right) // 2
        if arr[center] == key:
            return center
        elif arr[center] < key:
            left = center + 1
        else:
            right = center - 1
    return -1

arr = [1, 2, 4, 5, 6, 6, 9]

result = binary_search(arr, 4)

print(result)