s1 = 'ACAYKP'
s2 = 'CAPCAK'
l1, l2 = len(s1), len(s2)

g = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            g[i + 1][j + 1] = g[i][j] + 1
        else:
            g[i + 1][j + 1] = max(g[i + 1][j], g[i][j + 1])

r = []

while l1 > 0 and l2 > 0:
    if s1[l1 - 1] == s2[l2 - 1]:
        r.append(s1[l1 - 1])
        l1 -= 1
        l2 -= 1
    elif g[l1 - 1][l2] > g[l1][l2 - 1]:
        l1 -= 1
    else:
        l2 -= 1

print(g[-1][-1])
print(''.join([*reversed(r)]))