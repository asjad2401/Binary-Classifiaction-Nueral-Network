
def is_valid_move(matrix, visited, i, j):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0 and not visited[i][j]

def explore_maze(matrix, visited, i, j, steps, min_steps):
    rows, cols = len(matrix), len(matrix[0])

    if i == rows - 1 and j == cols - 1:
        min_steps[0] = min(min_steps[0], steps)
        return

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    for di, dj in directions:
        new_i, new_j = i + di, j + dj

        if is_valid_move(matrix, visited, new_i, new_j):
            visited[new_i][new_j] = True
            explore_maze(matrix, visited, new_i, new_j, steps + 1, min_steps)
            visited[new_i][new_j] = False

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # First, try without removing walls
    visited = [[False] * cols for _ in range(rows)]
    min_steps = [float('inf')]
    explore_maze(matrix, visited, 0, 0, 1, min_steps)

    # Now, try removing walls
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                matrix[i][j] = 0  # Try removing the wall
                visited = [[False] * cols for _ in range(rows)]
                min_steps_with_removal = [float('inf')]
                explore_maze(matrix, visited, 0, 0, 1, min_steps_with_removal)
                matrix[i][j] = 1  # Restore the wall

                min_steps[0] = min(min_steps[0], min_steps_with_removal[0])

    return min_steps[0]
