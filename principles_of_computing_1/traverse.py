GRID_HEIGHT = 4
GRID_WIDTH = 6

EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]


def traverse_grid(start_cell, direction, num_steps):
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        print("Processing cell:", (row, col), end='')
        print(" with value:", EXAMPLE_GRID[row][col])


def run_example():
    for row in range(GRID_HEIGHT):
        print(EXAMPLE_GRID[row])

    print('\nTraversing first row')
    traverse_grid((0, 0), (0, 1), GRID_WIDTH)

    print('\nTraversing second column')
    traverse_grid((0, 1), (1, 0), GRID_HEIGHT)

    print('\nTraversing second column in reverse order')
    traverse_grid((GRID_HEIGHT - 1, 1), (-1, 0), GRID_HEIGHT)

    print('\nTraversing diagonal')
    traverse_grid((0, 0), (1, 1), min(GRID_WIDTH, GRID_HEIGHT))


run_example()
