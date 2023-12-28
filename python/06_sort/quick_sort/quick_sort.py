import random
n = 10
arr = [random.randint(0, n) for _ in range(n)]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    lArr, eArr, rArr = [], [], []
    for i in arr:
        if i < p:
            lArr.append(i)
        elif i > p:
            rArr.append(i)
        else:
            eArr.append(i)
    return quick_sort(lArr) + eArr + quick_sort(rArr)

print(quick_sort(arr))