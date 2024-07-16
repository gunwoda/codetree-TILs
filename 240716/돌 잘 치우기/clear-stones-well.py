import itertools
from collections import deque

n,k,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

start_point = []

for i in range(k):
    start_point.append(list(map(int,input().split())))

stone = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            stone.append([i,j])

comb = itertools.combinations(stone,m)

dy = [0,0,1,-1]
dx = [1,-1,0,0]

max_count = 0

def bfs(y,x):
    global count
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count = count+1
                    q.append((ny,nx))

for i in comb:
    for p in i:
        y,x = p
        graph[y][x] = 0
    visited = [[0]*(n) for _ in range(n)]
    count = 0
    for k in start_point:
            r,c = k
            if visited[r-1][c-1] == 0:
                count = count+1
                bfs(r-1,c-1) 
    max_count = max(count,max_count)   
    for p in i:
        y,x = p
        graph[y][x] = 1

print(max_count)