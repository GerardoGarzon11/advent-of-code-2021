"""--- Day 9: Smoke Basin ---
"""


def format_line(line: str) -> list:
    return list(map(int, list(line.strip())))


def is_lowpoint(point_and_adjacents: tuple) -> bool:
    """Returns True if a particular point is smaller than all its adjacent points

    Args:
        point_and_adjacents (tuple): [First element is a point in the heightmap,
        second element is a list of the adjacent points]

    Returns:
        bool: [Is the point smaller than its adjacent points]
    """
    if point_and_adjacents[0] < min(point_and_adjacents[1]):
        return True

    return False


def multiple_three_largest_basins(largest: list) -> int:
    result = 1
    for basin in largest:
        result *= basin

    return result


def solve_part_1(heightmap: list) -> int:
    """Returns the sum of the risk levels of all low points in the heightmap.
    A low point is a location that is lower thatn any of its adjacent locations.
    An adjacent location can be: up, down, left, and right. (Diagonals do not count)

    Args:
        heightmap (list): [Representation of the floor of the nearby caves]

    Returns:
        int: [Sum of the risk levels of all low points in the heightmap]
    """
    risk_level_sum = 0

    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[i]) - 1):
            point_and_adjacents = (
                heightmap[i][j],
                [
                    heightmap[i - 1][j],
                    heightmap[i][j - 1],
                    heightmap[i][j + 1],
                    heightmap[i + 1][j],
                ],
            )
            if is_lowpoint(point_and_adjacents):
                risk_level_sum += heightmap[i][j] + 1

    return risk_level_sum


def solve_part_2(heightmap: list) -> int:
    """[Finds the three largest basins and multiplies their size together]

    Args:
        heightmap (list): [Representation of the floor of the nearby caves]

    Returns:
        int: [Multiplication of the size of the three largest basins]
    """
    # Each position in this 2D-list represents the basin each position belongs to
    basins = [[None] * len(l) for l in heightmap]
    # Each key-value pair here represents a basin number and the positions that belong to it
    basin_counts = {}
    # There are special cases in this solving process where to basins need to be merged
    # A link is [Basin A Index, Basin B Index] where Basin A index is always smaller than
    # Basin B index, so that Basin B can be merged into Basin A at the end
    links = []

    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[i]) - 1):
            # Is it a 9?
            if heightmap[i][j] < 9:
                up_basin = basins[i - 1][j]
                left_basin = basins[i][j - 1]
                # Are there existant basins around (up, left)
                if up_basin is not None or left_basin is not None:
                    # Assign to smallest numbered one
                    min_basin_index = min(
                        [b for b in [up_basin, left_basin] if b is not None],
                        default=None,
                    )
                    basins[i][j] = min_basin_index
                    basin_counts[min_basin_index].append(heightmap[i][j])

                    # Create a link if two existant basins "collide"
                    if (
                        up_basin is not None
                        and left_basin is not None
                        and (up_basin != left_basin)
                    ):
                        links.append(
                            [min([up_basin, left_basin]), max([up_basin, left_basin])]
                        )

                # New basin (or has none up or left)
                else:
                    # Special case: avoids the scenario where the next position to be checked
                    # has a distinct basin number up and left
                    if heightmap[i][j + 1] < 9 and heightmap[i - 1][j + 1] < 9:
                        diagonal_valid_basin = basins[i - 1][j + 1]
                        basins[i][j] = diagonal_valid_basin
                        basin_counts[diagonal_valid_basin].append(heightmap[i][j])
                    else:
                        basins[i][j] = len(basin_counts.values())
                        basin_counts[len(basin_counts.values())] = [heightmap[i][j]]

    # Merges "colliding" basins
    for link in reversed(links):
        small_basin = basin_counts[link[1]]
        basin_counts[link[0]] += small_basin
        basin_counts[link[1]] = []

    # Finds the three largest basins
    largest = []
    for basin in basin_counts.values():
        largest.append(len(basin))
        if len(largest) > 3:
            largest.remove(min(largest))

    return multiple_three_largest_basins(largest)


if __name__ == "__main__":
    heightmap = []
    with open("input9.txt") as f:
        # Add 9s all around the heightmap to avoid special cases (corners and edges)
        for line in f:
            heightmap.append([9] + format_line(line) + [9])

    # Add a line of 9s at the top and bottom of the heightmap
    heightmap.append([9] * len(heightmap[1]))
    heightmap.insert(0, [9] * len(heightmap[1]))

    print(
        f"The sum of the risk levels of all low points in the heightmap is: {solve_part_1(heightmap)}"
    )

    print(
        f"The result of multiplying together the sizes of the three largest basins is: {solve_part_2(heightmap)}"
    )
