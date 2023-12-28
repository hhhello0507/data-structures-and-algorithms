
n = int(input())
cnt = 0

row = [False for _ in range(n)]
col = [False for _ in range(n)]
f1 = [False for _ in range(n * 2)]
f2 = [False for _ in range(n * 2)]

cnt = 0
def A(row, col, f1, f2, i):
    global cnt
    for j in range(n):
        if not row[i] and not col[j] and not f1[i + j] and not f2[i - j + n]:
            newR = row[:]
            newC = col[:]
            newF1 = f1[:]
            newF2 = f2[:]
            newR[i] = True
            newC[j] = True
            newF1[i + j] = True
            newF2[i - j + n] = True
            if i < n - 1:
                A(newR, newC, newF1, newF2, i + 1)
            else:
                cnt += 1


A(row, col, f1, f2, 0)
print(cnt)