import random
n = 10
arr = [random.randint(0, n) for _ in range(n)]

def merge_sort(arr):
    def divide(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        divide(low, mid)
        divide(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        # 정렬
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        # 남은 거 넣기
        temp.extend(arr[l:mid])
        temp.extend(arr[h:high])

        # 적용하기
        arr[low: high] = temp

    divide(0, len(arr))
    return arr

print(merge_sort(arr))