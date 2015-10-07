import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    stack = []
    current_cell = random.randint(0, m.total_cells - 1)
    visited_cells = 1
    while visited_cells < m.total_cells:
        neighbors = m.cell_neighbors(current_cell)
        if neighbors:
            random_neighbor = random.randint(0, len(neighbors) - 1)
            m.connect_cells(current_cell, neighbors[random_neighbor][0], neighbors[random_neighbor][1])
            stack.append(current_cell)
            current_cell = neighbors[random_neighbor][0]
            visited_cells += 1
        else:
            current_cell = stack.pop()
        m.refresh_maze_view()
    m.sate = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
