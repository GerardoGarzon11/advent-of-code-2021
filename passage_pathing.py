"""--- Day 12: Passage Pathing ---
"""

from string import ascii_lowercase as lower_alphabet

POINT_TYPES = {"START": 0, "SMALL": 1, "BIG": 2, "END": 3}

part_2_rule = False


class Node:
    def __init__(self, name, type="start"):
        self.name = name
        self.type = type
        self.connections = []

    def add_connection(self, node):
        self.connections.append(node)

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nConnections: {self.connections}"


def get_point_type(name: str) -> int:
    """Returns the type of cave/point

    Args:
        name (str): [Name of cave/point]

    Returns:
        int: [Type of cave/point]
    """
    if name == "start":
        return POINT_TYPES["START"]
    elif name == "end":
        return POINT_TYPES["END"]
    elif name[0] in lower_alphabet:
        return POINT_TYPES["SMALL"]

    return POINT_TYPES["BIG"]


def get_number_of_small_caves_in_path(path):
    """Returns the number of small (lowercase) caves in path

    Args:
        path ([type]): [List of caves in path]

    Returns:
        [type]: [Number of small caves in path]
    """
    small_cave_count = 0
    for p in path:
        if p not in ["start", "end"]:
            if p[0] in lower_alphabet:
                small_cave_count += 1
    return small_cave_count


def has_small_caves_occurring_more_than_once(path: list) -> bool:
    """Validates if there are small caves being visited more than once in the path

    Args:
        path ([list]): [Current path]

    Returns:
        [bool]: [True if there are small caves appearing twice in path. False otherwise.]
    """
    cave_set = set(path)
    cave_counts = {}
    for cave in cave_set:
        cave_counts[cave] = path.count(cave)

    for key in cave_counts:
        if get_point_type(key) == 1:
            if cave_counts[key] > 1:
                return True

    return False


def travel(node: Node, path: list = []) -> int:
    """Traverses recursively the cave paths

    Args:
        node (Node): [Current cave]
        path (list, optional): [Current travelled path]. Defaults to [].

    Returns:
        [type]: [Depending on part_2_rule value: returns a number of paths or a number of
        small caves]
    """
    path.append(node.name)
    paths = 0
    for conn in node.connections:
        # A small node cannot be twice visited
        if conn.type == 2 or (conn.type == 1 and conn.name not in path):
            paths += travel(conn, path.copy())
        elif part_2_rule and (
            conn.type == 2
            or (conn.type == 1 and conn.name not in path)
            or (conn.type == 1 and not has_small_caves_occurring_more_than_once(path))
        ):
            paths += travel(conn, path.copy())
        elif conn.type == 3:
            # Process continues even if an end is found, so it's added and removed
            path.append(conn.name)
            # print(path)
            path.pop()
            if get_number_of_small_caves_in_path(path) < 2 and not part_2_rule:
                paths += 1
            else:
                paths += 1
        else:
            continue
    return paths


def solve_passage_pathing(nodes: dict) -> int:
    """Starts the travelling process

    Args:
        nodes (dict): [List of nodes]

    Returns:
        int: [Result of the process]
    """
    return travel(nodes["start"])


if __name__ == "__main__":
    nodes = {}
    with open("input12.txt") as f:
        for line in f:
            connection = line.strip().split("-")

            # Create point if it does not exist
            for point_name in connection:
                if point_name not in nodes.keys():
                    nodes[point_name] = Node(
                        name=point_name, type=get_point_type(point_name)
                    )

            # Create connections
            point_x, point_y = connection[0], connection[1]
            nodes[point_x].add_connection(nodes[point_y])
            nodes[point_y].add_connection(nodes[point_x])

    print(
        f"The solution for Passage Pathing, Part 1 is: {solve_passage_pathing(nodes)}"
    )
    part_2_rule = True
    print(
        f"The solution for Passage Pathing, Part 2 is: {solve_passage_pathing(nodes)}"
    )
