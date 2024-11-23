s1 = 'ABRACADABRA'
s2 = 'ECADADABRBCRDARA'
l1, l2 = len(s1), len(s2)

g = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            g[i + 1][j + 1] = g[i][j] + 1

m = max([max(i) for i in g])
print(m)