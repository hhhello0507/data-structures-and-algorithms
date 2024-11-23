from collections import deque

n = 7
a = [[] for _ in range(n)] # idx: 노드, i: 그 노드의 인접노드
v = [0 for _ in range(n)] # 진입차수

def topology_sort():

    q = deque()

    for (idx, i) in enumerate(v):
        if i == 0:
            q.append(idx)

    result = []


    for i in range(n):
        x = q.popleft()
        result.append(x)
        for j in a[x]:
            v[j] -= 1
            if v[j] == 0:
                q.append(j)
    
    print([i + 1 for i in result])


if __name__ == '__main__':
    a[0].append(1)
    v[1] += 1
    a[0].append(4)
    v[4] += 1
    a[1].append(2)
    v[2] += 1
    a[2].append(3)
    v[3] += 1
    a[3].append(5)
    v[5] += 1
    a[4].append(5)
    v[5] += 1
    a[5].append(6)
    v[6] += 1
    # for i in a:
        # print(i)
    topology_sort()