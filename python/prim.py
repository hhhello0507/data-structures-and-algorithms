import heapq

N = 7  # 정점의 개수
G = {
    0: [(6, 12), (3, 28), (1, 67), (4, 17)],
    1: [(3, 24), (4, 62)],
    2: [(4, 20), (5, 37)],
    3: [(0, 28), (1, 24), (6, 13)],
    4: [(0, 17), (1, 62), (2, 20), (5, 45), (6, 73)],
    5: [(2, 37), (4, 45)],
    6: [(0, 12), (3, 13), (4, 73)]
}

visited = [False] * N
H = [(0, 0)] # (가중치, 시작 정점)
sum = 0 # MST 가중치 총합

while H:
    w, u = heapq.heappop(H) # w가 가장 작은 거

    # 이미 방문한 정점이면 스킵
    if visited[u]:
        continue

    visited[u] = True # 방문 처리
    sum += w # MST에 추가된 간선의 가중치 더하기

    # 현재 정점에 연결된 모든 간선 탐색
    for v, w in G[u]:
        if not visited[v]:
            heapq.heappush(H, (w, v))

print(sum)