# import matplotlib.pyplot as plt
# import numpy as np
# import time

# # Grid definition: 0 = free, 1 = obstacle
# rows, cols = 10, 10
# grid = np.zeros((rows, cols))
# grid[3, 3:7] = 1
# grid[6, 1:5] = 1
# grid[1:4, 8] = 1

# start = (0, 0)

# # Directions: right, down, left, up
# directions = [(0,1),(1,0),(0,-1),(-1,0)]

# visited = set()

# def is_valid(cell):
#     x, y = cell
#     return 0 <= x < rows and 0 <= y < cols and grid[x, y] == 0 and cell not in visited

# # DFS traversal
# def dfs(cell):
#     visited.add(cell)
#     yield cell  # Yield current cell for visualization
#     for dx, dy in directions:
#         neighbor = (cell[0] + dx, cell[1] + dy)
#         if is_valid(neighbor):
#             yield from dfs(neighbor)

# # Visualization
# plt.ion()
# fig, ax = plt.subplots(figsize=(6,6))
# ax.imshow(grid, cmap='Greys', origin='upper')

# agent, = ax.plot([], [], 'ro', markersize=12)  # Agent marker

# for step, cell in enumerate(dfs(start)):
#     x, y = cell
#     agent.set_data(y, x)
#     plt.draw()
#     plt.pause(0.1)  # Adjust speed
#     if step == 0:
#         ax.scatter(y, x, marker='s', color='green', s=100, label="Start")
# ax.legend()
# plt.ioff()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Grid size
rows, cols = 10, 10
grid = np.zeros((rows, cols))  # 0 = free, 1 = obstacle

# Input obstacles manually
num_obstacles = int(input("How many obstacles? "))
for _ in range(num_obstacles):
    x, y = map(int, input("Enter obstacle coordinates (row col): ").split())
    if 0 <= x < rows and 0 <= y < cols:
        grid[x, y] = 1

start = (0, 0)  # Starting point
directions = [(0,1),(1,0),(0,-1),(-1,0)]  # Right, Down, Left, Up
visited = set()

# Check valid move
def is_valid(cell):
    x, y = cell
    return 0 <= x < rows and 0 <= y < cols and grid[x, y] == 0 and cell not in visited

# DFS to visit every free space
def dfs(cell):
    visited.add(cell)
    yield cell
    for dx, dy in directions:
        neighbor = (cell[0] + dx, cell[1] + dy)
        if is_valid(neighbor):
            yield from dfs(neighbor)

# Visualization
plt.ion()
fig, ax = plt.subplots(figsize=(6,6))
ax.imshow(grid, cmap='Greys', origin='upper')
agent, = ax.plot([], [], 'ro', markersize=12)  # Agent marker
ax.scatter(start[1], start[0], marker='s', color='green', s=100, label="Start")
ax.legend()

for cell in dfs(start):
    x, y = cell
    agent.set_data(y, x)
    plt.draw()
    plt.pause(0.1)  # Speed of movement

plt.ioff()
plt.show()
