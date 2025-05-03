import heapq

# Hàm tính heuristic (khoảng cách Manhattan)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Thuật toán A* tìm đường đi
def a_star(maze, start, end):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))  # (f_cost, g_cost, position)
    came_from = {}
    g_costs = {start: 0}
    
    while open_list:
        _, g_cost, current = heapq.heappop(open_list)
        
        if current == end:
            # Tìm được đường đi, xây dựng lại đường đi từ end đến start
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Trả về đường đi từ start đến end
        
        closed_list.add(current)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[1]][neighbor[0]] == 0:
                if neighbor in closed_list:
                    continue
                
                tentative_g_cost = g_cost + 1  # Di chuyển từ 1 ô sang 1 ô kế tiếp (chi phí 1)
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_cost, tentative_g_cost, neighbor))
                    came_from[neighbor] = current
                
    return None  # Không tìm thấy đường đi

# Ví dụ sử dụng A* để tìm đường đi trong maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

path = a_star(maze, start, end)
if path:
    print("Đường đi:", path)
else:
    print("Không có đường đi khả dụng")
