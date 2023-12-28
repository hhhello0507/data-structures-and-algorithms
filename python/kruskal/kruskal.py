
def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = get_parent(a), get_parent(b)
    if a > b: parent[a] = b
    else: parent[b] = a

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

class Edge:
    def __init__(self, a, b, w):
        self.node = [a, b]
        self.w = w


n = 7
m = 11
v = [
    Edge(0, 6, 12),
    Edge(0, 3, 28),
    Edge(0, 1, 67),
    Edge(0, 4, 17),
    Edge(1, 3, 24),
    Edge(1, 4, 62),
    Edge(2, 4, 20),
    Edge(2, 5, 37),
    Edge(3, 6, 13),
    Edge(4, 5, 45),
    Edge(4, 6, 73)
]
parent = [i for i in range(n)]
v = sorted(v, key=lambda x: x.w)

sum = 0
for i in v:
    # 연결 되어있지 않으면?
    if not find_parent(i.node[0], i.node[1]):
        sum += i.w # 1) 더하기
        union_parent(i.node[0], i.node[1]) # 2) 연결하기

print(sum)
