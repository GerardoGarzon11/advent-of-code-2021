"""--- Day 1: Sonar Sweep ---
"""


def count_window_increments(input_array, window_size):
    """Returns the number of times the current window had a larger sum than the previous one

    Args:
        input_array (List): List of values (integers)
        window_size (int): Size of the window

    Returns:
        [int]: Number of increments
    """

    return sum(
        [
            1
            for x in range(0, len(input_array) - window_size)
            if input_array[x] < input_array[x + window_size]
        ]
    )


if __name__ == "__main__":
    input_array = []
    with open("input1.txt", "r") as f:
        for line in f:
            input_array.append(int(line))
    print(
        f"The result of 'Sonar Sweep #1' is {count_window_increments(input_array, 1)}"
    )
    print(
        f"The result of 'Sonar Sweep #2' is {count_window_increments(input_array, 3)}"
    )
