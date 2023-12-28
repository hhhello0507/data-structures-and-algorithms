import random
n = 10
arr = [random.randint(0, n) for _ in range(n)]
for i in range(1, n):
    key = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[j] <= arr[j + 1]:
            break
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    arr[j] = key
        
print(arr)