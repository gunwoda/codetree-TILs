import sys
from collections import deque

n,k = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
start_point = []
for i in range(k):
    start_point.append(list(map(int,input().split())))

dy = [0,0,1,-1]
dx = [1,-1,0,0]


def bfs(y,x):
    q = deque()
    q.append((y,x))
    count = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<= ny<n and 0<= nx<n:
                if visited[ny][nx] == 0 and graph[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count = count+1
                    q.append((ny,nx))
    return count
total_score = 0
visited = [[0]*(n) for _ in range(n)]
for i in start_point:
    y,x = i
    total_score = total_score+bfs(y,x)
print(total_score)