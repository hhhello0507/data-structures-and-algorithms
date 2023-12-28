n = 11
id = 0 # 노드 별 고유키
d = [0 for _ in range(n)]
v = [False for _ in range(n)] # 종료(방문) 여부
a = [[] for _ in range(n)] # idx: 노드, i: 그 노드의 인접노드
SCC = [] # SCC 
s = [] # 스택

def dfs(x):
    global id
    id += 1
    d[x] = id
    s.append(x)

    parent = d[x]
    for i in a[x]:
        if d[i] == 0:
            parent = min(parent, dfs(i))
        elif not v[i]: # d[i]가 0이 아니고(진행 중인 노드이고) & 종료(방문) 되지 않았다면?
            parent = min(parent, d[i])

    if parent == d[x]:
        scc = []
        # SCC에 삽입 후 한꺼번에 종료(방문) 처리
        while True:
            t = s.pop()
            scc.append(t)
            v[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent


if __name__ == '__main__':
    a[0].append(1)
    a[1].append(2)
    a[2].append(0)
    a[3].append(1)
    a[3].append(4)
    a[4].append(6)
    a[5].append(4)
    a[6].append(5)
    a[7].append(4)
    a[7].append(8)
    a[8].append(9)
    a[9].append(10)
    a[10].append(2)
    a[10].append(7)

    # 모든 노드 중 진입차수가 0인 노드를 찾아 dfs 수행
    for i in range(n):
        if d[i] == 0:
            dfs(i)
        
    print(f'SCC count - {len(SCC)}')
    for (idx, i) in enumerate(SCC):
        print(f'{idx + 1}번째 SCC')
        for j in i:
            print(end=f'{j + 1} ')
        print()
