"""--- Day 5: Hydrothermal Venture ---
"""


def get_number_of_dangerous_points(coordinates: list, include_diagonals=False) -> int:
    """Returns the number of dangerous points in the Hydrothermal Diagram

    Args:
        coordinates (list): [List of coordinates]
        include_diagonals (bool, optional): [Include diagonal lines or not]. Defaults to False.

    Returns:
        int: [Number of dangerous points]
    """
    diagram = [[0] * 1000 for i in range(1000)]
    for c in coordinates:
        # if x1 = x2 or y1 = y2, but not both, it is a horizontal or vertical line
        if (c[0][0] == c[1][0] or c[0][1] == c[1][1]) and (
            c[0][0] != c[1][0] or c[0][1] != c[1][1]
        ):
            # Vertical
            if c[0][0] == c[1][0]:
                x = c[0][0]
                for y_ in range(min(c[0][1], c[1][1]), max(c[0][1], c[1][1]) + 1):
                    diagram[x][y_] += 1
            # Horizontal
            else:
                y = c[0][1]
                for x_ in range(min(c[0][0], c[1][0]), max(c[0][0], c[1][0]) + 1):
                    diagram[x_][y] += 1
        elif include_diagonals:
            x_step = 1 if c[0][0] < c[1][0] else -1
            y_step = 1 if c[0][1] < c[1][1] else -1
            # Diagonal
            tmp_start = c[0]
            while tmp_start != c[1]:
                diagram[tmp_start[0]][tmp_start[1]] += 1
                tmp_start[0] += x_step
                tmp_start[1] += y_step
            diagram[c[1][0]][c[1][1]] += 1

    counter = 0
    for row in diagram:
        for cell in row:
            counter += 1 if cell > 1 else 0

    return counter


def get_coordinates(line: str) -> list:
    """Returns a list with point A and point B

    Args:
        line (str): [Coordinates with input format]

    Returns:
        list: [Point A and Point B of line]
    """
    coordinates = []
    split_line = line.split(" -> ")
    p1 = list(map(int, split_line[0].split(",")))
    p2 = list(map(int, split_line[1].split(",")))
    return (p1, p2)


if __name__ == "__main__":
    coordinates = []

    with open("input5.txt") as f:
        for line in f.readlines():
            new_coordinate = get_coordinates(line)
            coordinates.append(new_coordinate)

    print(
        f"Hydrothermal Venture Part 1, result: {get_number_of_dangerous_points(coordinates)}"
    )
    print(
        f"Hydrothermal Venture Part 2, result: {get_number_of_dangerous_points(coordinates, include_diagonals=True)}"
    )
