import random
n = 10
arr = [random.randint(0, n) for _ in range(n)]

for i in range(n):
    mnIdx = i
    for j in range(i, n):
        if arr[j] < arr[mnIdx]:
            mnIdx = j
    arr[mnIdx], arr[i] = arr[i], arr[mnIdx]

print(arr)