"""--- Day 11: Dumbo Octopus ---
"""


def increase_by_one(x):
    return x + 1 if x != -1 else x


def increase_energy_of_adjacent_octupuses(grid: list, position: tuple) -> list:
    """
    (x-1, y-1)  (x-1, y)    (x-1, y+1)
    (x, y-1)    (x, y)      (x, y+1)
    (x+1, y-1)  (x+1, y)    (x+1, y+1)
    """
    x = position[0]
    y = position[1]

    to_update = [
        [x - 1, y - 1],
        [x - 1, y],
        [x - 1, y + 1],
        [x, y - 1],
        [x, y + 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1],
    ]

    try:
        for p in to_update:
            grid[p[0]][p[1]] += (
                1 if grid[p[0]][p[1]] != -1 and grid[p[0]][p[1]] < 10 else 0
            )

        grid[x][y] += 1

        for p in to_update:
            if grid[p[0]][p[1]] == 10:
                grid = increase_energy_of_adjacent_octupuses(
                    grid, position=(p[0], p[1])
                )

    except ValueError:
        print("Index does not exist")

    return grid


def count_flashes_and_adjust_energy_levels(grid):
    flashes = 0

    # Starts at 1, ends at -1, to skip helper cells
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            if grid[x][y] > 9 and grid[x][y] != -1:
                flashes += 1
                grid[x][y] = 0

    return (grid, flashes)


def get_number_of_flashes(grid: list, steps: int) -> int:

    flashes = 0

    # Add helper cells
    for x in range(len(grid)):
        grid[x].append(-1)  # at the end
        grid[x].insert(0, -1)  # at the start

    # Add helper line at the end and at the start
    grid.append([-1] * len(grid[0]))
    grid.insert(0, [-1] * len(grid[0]))

    while steps:
        # 1 - The energy of each octopus increases by 1
        for x in range(1, len(grid) - 1):
            grid[x] = list(map(increase_by_one, grid[x]))

        # 2 - Octopuses with energy greater than 9 flash
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                # Skip helper cells
                if grid[x][y] == -1:
                    continue
                if grid[x][y] == 10:
                    grid = increase_energy_of_adjacent_octupuses(grid, position=(x, y))

        step_results = count_flashes_and_adjust_energy_levels(grid)

        grid = step_results[0]
        flashes += step_results[1]

        steps -= 1

    return flashes


if __name__ == "__main__":
    octopus_grid = []
    with open("input11.txt") as f:
        for line in f:
            octopus_grid.append(list(map(int, list(line.strip()))))

    print(
        f"The total number of flashes after a 100 steps is: {get_number_of_flashes(octopus_grid, 100)}"
    )
