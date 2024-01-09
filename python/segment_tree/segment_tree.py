import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        return T[node]

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node] = min([lc, rc]) # condition
    return T[node]


def get_min(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return 1_000_000_001

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node]

    lc = get_min(node * 2, s, (s + e) // 2, s1, e1)
    rc = get_min(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return min([lc, rc]) # condition

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
T = [1_000_000_001 for _ in range(3000000)]

init_tree(1, 0, n - 1)

# update
for _ in range(m):
    b, c = map(int, input().split())

    print(get_min(1, 0, n - 1, b - 1, c - 1))
