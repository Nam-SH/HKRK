from collections import deque


def minimumMoves(grid, startY, startX, goalY, goalX):
    n = 3
    q = deque()
    q.append((startY, startX, 0, -1))
    visit = {(startY, startX): 0}
    dy, dx = [-1, 0, 0, 1, 1], [0, 1, -1, 0, 1]

    def check(i, j, curr_dist):
        if not (0 <= i < n > j >= 0): return False
        if grid[i][j] == 'X': return False
        if (i, j) not in visit: return True
        if (i, j) in visit and curr_dist <= visit[(i, j)]: return True
        return False

    while q:
        y, x, dist, before_d = q.pop()
        for k in range(4):
            nxt = 0 if (dy[k], dx[k]) == (dy[before_d], dx[before_d]) else 1
            ty = y + dy[k]; tx = x + dx[k]; nxt_dist = dist + nxt
            if check(ty, tx, nxt_dist):
                visit[(ty, tx)] = nxt_dist
                q.appendleft((ty, tx, nxt_dist, k))
    return visit[(goalY, goalX)]


print(minimumMoves([[".", "X", "."], [".", "X", "."], [".", ".", "."]], 0, 0, 0, 2))
