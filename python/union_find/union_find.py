n = 10
parent = [i for i in range(n)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if (a < b): parent[b] = a
    else: parent[a] = b

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

union_parent(0, 1)
union_parent(1, 2)
union_parent(2, 3)
union_parent(4, 5)
union_parent(5, 6)
union_parent(6, 7)
print(find_parent(0, 1))
print(find_parent(3, 4))
