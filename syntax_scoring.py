"""--- Day 10: Syntax Scoring ---
"""

from os import error


OPENING_CHARS = "([{<"
CLOSING_CHARS = ")]}>"
OPEN_CLOSE = {")": "(", "]": "[", "}": "{", ">": "<"}
POINT_SYSTEM = {")": 3, "]": 57, "}": 1197, ">": 25137}


def get_total_syntax_error_score(lines):
    error_score = 0
    for line in lines:
        open = []
        for char in line:
            if char in OPENING_CHARS:
                open.append(char)
            elif char in CLOSING_CHARS:
                if OPEN_CLOSE[char] != open[-1]:
                    error_score += POINT_SYSTEM[char]
                    break
                else:
                    open.pop()

    return error_score


if __name__ == "__main__":
    lines = []
    with open("input10.txt") as f:
        for text_line in f:
            lines.append(list(text_line))

    print(f"The result for Part 1 is: {get_total_syntax_error_score(lines)}")
