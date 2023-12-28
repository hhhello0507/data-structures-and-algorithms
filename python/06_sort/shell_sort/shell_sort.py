import random
n = 10
arr = [random.randint(0, n) for _ in range(n)]

n = len(arr) # 8
gap = len(arr) // 2 # 4, 2, 1, 0

# 갭 마다
while gap > 0:
    # 선택 정렬 수행
    for i in range(gap, n):
        key = arr[i]
        j = i - gap
        # ing...
        while j >= 0 and arr[j] > key:
            arr[j + gap] = arr[j]
            j -= gap
        arr[j + gap] = key
    gap //= 2
print(arr)