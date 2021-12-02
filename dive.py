"""--- Day 2: Dive! ---
"""


def dive(steps, use_aim=False):
    """Calculates the final horizontal position and depth using the steps provided in [steps]
        and returns the product of both

    Args:
        steps ([list]): [List of steps to be followed]
        use_aim (bool, optional): [Flag used to determine if aim will be used]. Defaults to False.

    Returns:
        [int]: [Product of final horizontal position and depth]
    """
    x, y, aim = 0, 0, 0

    for step in steps:
        if step[0] == "forward":
            x += int(step[1])
            if use_aim:
                y += aim * int(step[1])
        elif step[0] == "down":
            if use_aim:
                aim += int(step[1])
            else:
                y += int(step[1])
        else:
            if use_aim:
                aim -= int(step[1])
            else:
                y -= int(step[1])

    return x * y


if __name__ == "__main__":
    input = []
    with open("input2.txt") as f:
        for line in f:
            input.append(line.split())

    print(f"The result of Dive! #1 is: {dive(input, use_aim=False)}")
    print(f"The 2nd result of Dive! #2 is: {dive(input, use_aim=True)}")
