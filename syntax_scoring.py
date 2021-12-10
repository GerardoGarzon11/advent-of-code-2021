"""--- Day 10: Syntax Scoring ---
"""


OPENING_CHARS = "([{<"
CLOSING_CHARS = ")]}>"
OPEN_CLOSE = {")": "(", "]": "[", "}": "{", ">": "<"}
ERROR_POINT_SYSTEM = {")": 3, "]": 57, "}": 1197, ">": 25137}
INCOMPLETE_POINT_SYSTEM = {"(": 1, "[": 2, "{": 3, "<": 4}


def get_error_and_incompletion_scores(lines: list) -> tuple:
    """Calculates the error and incompletion scores

    Args:
        lines (list): [Lines of the navigation subsystem]

    Returns:
        tuple: [First element is the error score, the second one is the middle incompletion score]
    """
    error_score = 0
    incomplete_scores = []
    for line in lines:
        open = []
        is_erroneous = False
        for char in line:
            if char in OPENING_CHARS:
                open.append(char)
            elif char in CLOSING_CHARS:
                if OPEN_CLOSE[char] != open[-1]:
                    error_score += ERROR_POINT_SYSTEM[char]
                    is_erroneous = True
                    break
                else:
                    open.pop()

        if not is_erroneous:
            # Solve incompletion
            incomplete_scores.append(0)
            for i in range(len(open) - 1, -1, -1):
                incomplete_scores[-1] *= 5
                incomplete_scores[-1] += INCOMPLETE_POINT_SYSTEM[open[i]]

    middle_score = sorted(incomplete_scores)[len(incomplete_scores) // 2]

    return (error_score, middle_score)


if __name__ == "__main__":
    lines = []
    with open("input10.txt") as f:
        for text_line in f:
            lines.append(list(text_line))

    results = get_error_and_incompletion_scores(lines)

    print(f"The result for Part 1 is: {results[0]}")
    print(f"The result for Part 2 is: {results[1]}")
