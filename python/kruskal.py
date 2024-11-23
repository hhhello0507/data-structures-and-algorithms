from union_find import (
    get_parent,
    find_parent,
    union_parent
)
from edge import Edge

N = 7 # 정점의 개수
parent = [i for i in range(N)]

G = [
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
G = sorted(G, key=lambda x: x.w)
sum = 0

for v in G:
    # 연결 되어있지 있으면(사이클 방지)
    if find_parent(parent, v.s, v.e): continue

    sum += v.w # 1) 가중치 더하기
    union_parent(parent, v.s, v.e) # 2) 연결

print(sum)
print(parent)