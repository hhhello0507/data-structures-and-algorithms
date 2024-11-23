def get_parent(parent, x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a, b = get_parent(parent, a), get_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def find_parent(parent, a, b):
    return get_parent(parent, a) == get_parent(parent, b)

if __name__ == '__main__':
    n = 10
    parent = [i for i in range(n)]

    union_parent(parent, 0, 1)
    union_parent(parent, 1, 2)
    union_parent(parent, 2, 3)
    union_parent(parent, 4, 5)
    union_parent(parent, 5, 6)
    union_parent(parent, 6, 7)

    print(parent)
    print(find_parent(parent, 0, 1))
    print(find_parent(parent, 3, 4))
