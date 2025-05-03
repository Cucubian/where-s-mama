from collections import deque

def bfs(grid, start, end):
    queue = deque([start])
    visited = set([start])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False
