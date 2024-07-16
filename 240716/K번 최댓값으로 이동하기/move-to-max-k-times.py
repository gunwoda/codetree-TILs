import sys
from collections import deque

input = sys.stdin.readline


n,k = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
r,c = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a,b,limit):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    max_v = 0
    max_x = b
    max_y = a
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx]<limit and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                    if max_v<graph[ny][nx]:
                        max_v = graph[ny][nx]
                        max_x = nx
                        max_y = ny
                    elif max_v == graph[ny][nx]:
                        if max_y>ny:
                            max_y = ny
                            max_x = nx
                        elif max_y==ny:
                            if max_x>nx:
                                max_x = nx
    return max_y,max_x

visited = [[0]*(n) for _ in range(n)]
x,y = bfs(r-1,c-1,graph[r-1][c-1])

for i in range(k-1):
    visited = [[0]*(n) for _ in range(n)]
    y,x = bfs(y,x,graph[y][x])
print(y+1,x+1)