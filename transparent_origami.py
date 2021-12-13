"""--- Day 13: Transparent Origami ---
"""


def add_dots(paper: list, dots: list) -> None:
    for dot in dots:
        paper[dot[1]][dot[0]] = "#"


def combine_horizontal_line(line_a: list, line_b: list) -> list:
    combined_line = []
    for x in range(len(line_a)):
        if "#" in line_a[x] or "#" in line_b[x]:
            combined_line.append("#")
        else:
            combined_line.append(".")
    return combined_line


def fold_up(paper: list, fold_along: int) -> list:
    up = paper[:fold_along]
    down = paper[(fold_along + 1) :]
    folded = []

    for l in range(fold_along - 1):
        if l >= len(up) or l >= len(down):
            if l > len(up):
                down_line = down[-1 - l]
                up_line = ["."] * len(down_line)
            else:
                up_line = up[l]
                down_line = ["."] * len(up_line)
        else:
            up_line = up[l]
            down_line = down[-1 - l]
        combined_line = combine_horizontal_line(up_line, down_line)
        folded.append(combined_line)

    return folded


def fold_left(paper: list, fold_along: int) -> list:
    folded = []

    for y in range(len(paper)):
        folded.append([])
        left = paper[y][:fold_along]
        right = paper[y][(fold_along + 1) :]
        # Complete if len(left) != len(right)
        if len(left) != len(right):
            diff = abs(len(left) - len(right))
            if len(left) < len(right):
                left = (["."] * diff) + left
            else:
                right = right + (["."] * diff)
        for l in range(fold_along):
            if "#" in left[l] or "#" in right[-(l + 1)]:
                folded[y].append("#")
            else:
                folded[y].append(".")

    return folded


def count_visible_dots(paper: list) -> int:
    visible_dots = 0
    for line in paper:
        visible_dots += line.count("#")
    return visible_dots


def solve_part_1(dimensions: list, instructions: list, dots: list) -> int:
    paper = [["."] * (dimensions[0] + 1) for y in range(0, dimensions[1] + 1)]

    add_dots(paper, dots)

    for instruction in instructions:
        if "y" in instruction:
            paper = fold_up(paper.copy(), int(instruction[2:]))
        else:
            paper = fold_left(paper.copy(), int(instruction[2:]))
        print(
            f"There are {count_visible_dots(paper)} visible after folding at {instruction}.\n"
        )

    return count_visible_dots(paper)


if __name__ == "__main__":
    folding_instructions = []
    dots = []
    paper_dimensions = [0, 0]
    with open("input13.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif "fold" in line:
                folding_instructions.append(line[11:])
            else:
                new_dot_pair = list(map(int, line.split(",")))
                dots.append(new_dot_pair)

                if new_dot_pair[0] > paper_dimensions[0]:
                    paper_dimensions[0] = new_dot_pair[0]
                if new_dot_pair[1] > paper_dimensions[1]:
                    paper_dimensions[1] = new_dot_pair[1]

    print(
        f"The answer for Part 1 of the problem is: {solve_part_1(paper_dimensions, folding_instructions, dots)}"
    )
