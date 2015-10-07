import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    stack = []
    current_cell = 0
    visited_cells = 0
    while current_cell != (m.total_cells - 1):
        neighbors = m.cell_neighbors(current_cell)
        if neighbors:
            random_neighbor = random.randint(0, len(neighbors) - 1)
            new_cell = neighbors[random_neighbor][0]
            compass = neighbors[random_neighbor][1]
            m.visit_cell(current_cell, new_cell, compass)
            stack.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = stack.pop()
        m.refresh_maze_view()
    m.sate = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
