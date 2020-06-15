from collections import deque


class Graph:
    num = 0

    def __init__(self, num):
        self.num = num
        self.lst = [[] for _ in range(num)]

    def connect(self, x, y):
        self.lst[x] += [y]
        self.lst[y] += [x]

    def find_all_distances(self, start):
        q = deque()
        q.append(start)
        visit = [-1] * self.num
        visit[start] = 0
        while q:
            curr = q.popleft()
            for i in self.lst[curr]:
                if visit[i] == -1:
                    visit[i] = visit[curr] + 6
                    q.append(i)
        print(*[val for (idx, val) in enumerate(visit) if idx != start])


for i in range(int(input())):
    n, m = map(int, input().split())
    graph = Graph(n)

    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)

    s = int(input())
    graph.find_all_distances(s - 1)
