"""--- Day 15: Chiton --
"""

# Errors
# 1 - build_node_grid(): started building without having the function design ready
# 2 - appended wrong variable to risk variable in line 2 of traverse
# 3 - conditions inside traverse() were evaluating elements that could be None. Switched conditions.
# 4 - switching conditions did not work, created a new if statement
# 5 - "is None" condition was evaluating the attribute, not the existence of the Node
# 6 - Recursive calls to traverse were all calling Node.left
# 7 - Recursive calls to traverse were receiving Node.left.id (int) instead of Node.left (Node)
# 8 - Condition for up direction was checking against the node, not the existance of the id in visited
# 9 - Traverse algorithm not working

from collections import OrderedDict

import sys

min_path = -1
current_best = -1


class Node:
    def __init__(
        self, id: str, risk: int, left=None, right=None, up=None, down=None
    ) -> None:
        self.id = id
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.risk = risk
        self.min = sys.maxsize
        self.visited = False

    def get_sorted_nodes(self):
        nodes = {}
        for n in [self.left, self.right, self.up, self.down]:
            if n is not None:
                nodes[f"{n.risk}{n.id}"] = n
        return OrderedDict(sorted(nodes.items()))


def build_node_grid() -> Node:
    """Builds the node grid using the data from the input file

    Returns:
        Node: [Start node of the node grid]
    """
    lines = open("input15.txt", "r").readlines()
    line_list = []
    x, y = 0, 0

    # build a 2D list with the nodes
    for line in lines:
        line_list.append([])
        x = 0
        for c in line.strip():
            new_node = Node(id=f"{x}_{y}", risk=int(c))
            line_list[-1].append(new_node)
            x += 1
        y += 1

    # link the nodes
    for i in range(len(line_list)):
        for j in range(len(line_list[i])):
            # First in line has no left node
            if j != 0:
                line_list[i][j].left = line_list[i][j - 1]
            # Nodes in first line have no up node
            if i != 0:
                line_list[i][j].up = line_list[i - 1][j]
            # Last in line has no right node
            if j != len(line_list[i]) - 1:
                line_list[i][j].right = line_list[i][j + 1]
            # Nodes in last line have no down node
            if i != len(line_list) - 1:
                line_list[i][j].down = line_list[i + 1][j]

    start_node = line_list[0][0]
    return start_node


def traverse(node: Node, start: bool = False, prev: int = 0) -> int:
    global current_best
    node.visited = True

    with open("log.txt", "a") as f:
        changed = False
        min_proposal = prev + node.risk

        if start:
            node.min = prev
        else:
            if node.min > prev + node.risk:
                node.min = min_proposal
                changed = True

        if node.down is None and node.right is None:  # you reached the last_one
            if current_best > node.min or current_best == -1:
                current_best = node.min
                print(current_best)
        elif changed or start:
            sorted_nodes = node.get_sorted_nodes()
            for n in sorted_nodes.values():
                if (
                    node.min + n.risk < current_best
                    or current_best == -1
                    and n.min > node.min + n.risk
                ):
                    traverse(n, prev=node.min)


def solve_part_1(start_node: Node) -> int:
    traverse(node=start_node, start=True)
    print(current_best)


if __name__ == "__main__":
    start_node = build_node_grid()

    solve_part_1(start_node)
