#!/usr/bin/python3
"""Island Perimeter """


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (List[List[int]]): A 2D grid containing 0s and 1s.

    Returns:
        int: The perimeter of the island.
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    perimeter = 0
    for i in range(row):
        for j in range(col):
            assert grid[i][j] in (0, 1), "Grid values must be 0 or 1"
            if grid[i][j] == 1:
                perimeter += 4  # Count all sides of a cell

                if i > 0 and grid[i - 1][j] == 1:
                    # Deduct two sides if there's an adjacent cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Deduct two sides if there's an adjacent cell to the left
                    perimeter -= 2
    return perimeter
