"""--- Day 14: Extended Polymerization ---
"""

global_rules = None
solution = {}


def parseData() -> tuple:
    """Reads the input file and returns a tuple with the formatted data

    Returns:
        [tuple]: [Formatted data]
    """
    with open("input14.txt") as f:
        template, raw_rules = f.read().split("\n\n")
        rules = {}
        for r in raw_rules.splitlines():
            split = r.split(" -> ")
            rules[split[0]] = split[1]

    return (template, rules)


def get_counts_dictionary(elements: set) -> dict:
    """Returns a dictionary where each key is a unique letter, and will store the number
    of times it appears in the final polymer

    Args:
        elements (set): [Results of every polymer rule (what every pair equals to/will add)]

    Returns:
        dict: [Dictionary of unique letters]
    """
    elem_dict = {}
    for e in elements:
        elem_dict[e] = 0
    return elem_dict


def solve(pair: str, element: str, rem_steps: int) -> int:
    """Receives a {pair} of elements. If the amount of times {element} appears in this particular {pair}
    with this particular {rem_steps} remaining, it returns it. Otherwise it invokes this method
    recursively.

    Args:
        pair (str): [Pair to be analyzed]
        letter (str): [Letter to be found in pair]
        rem_steps (int): [Number of remaining steps]

    Returns:
        int: [description]
    """
    if pair + f"{rem_steps}" + element in solution.keys():
        return solution[pair + f"{rem_steps}" + element]

    if rem_steps == 0:
        solution[pair + f"{rem_steps}" + element] = 1 if element in pair[1] else 0
        return 1 if element in pair[1] else 0
    else:
        solution[pair + f"{rem_steps}" + element] = solve(
            pair[0] + global_rules[pair], element, rem_steps - 1
        ) + solve(global_rules[pair] + pair[1], element, rem_steps - 1)
        return solution[pair + f"{rem_steps}" + element]


def grow_polymer(template: str, rules: dict, steps: int = 10) -> dict:
    """Calculates the number of times each element appears in the grown polymer after {steps} steps

    Args:
        template (str): [Base polymer]
        rules (dict): [Growth rules]
        steps (int, optional): [Number of steps]. Defaults to 10.

    Returns:
        dict: [Dictionary with each unique element and the number of times it appears in the grown polymer after {steps} steps]
    """
    letter_counts = get_counts_dictionary(set(rules.values()))
    for letter in letter_counts.keys():
        sum_ = 0
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            sum_ += solve(pair, letter, rem_steps=steps)
        if template[0] == letter:
            letter_counts[letter] = sum_ + 1
        else:
            letter_counts[letter] = sum_

    return letter_counts


def get_difference_between_most_common_and_least_common(polymer: dict) -> int:
    """Returns the difference between the number of appearances of the most common element
    and the least common one.

    Args:
        polymer (dict): [Dictionary with the number of appearances of each unique element]

    Returns:
        int: [Difference between the number of appearances of the most common element
    and the least common one.]
    """
    most_common, least_common = -1, -1
    for v in polymer.values():
        if v > most_common:
            most_common = v
        if v < least_common or least_common == -1:
            least_common = v

    return most_common - least_common


if __name__ == "__main__":
    parseData = parseData()
    template = parseData[0]
    rules = parseData[1]
    global_rules = rules

    grown_polymer = grow_polymer(template, rules, steps=10)

    print(
        f"The difference between the quantity of the most common element and the quantity of the least common element is: {get_difference_between_most_common_and_least_common(grown_polymer)}"
    )

    grown_polymer = grow_polymer(template, rules, steps=40)

    print(
        f"The difference after 40 steps is: {get_difference_between_most_common_and_least_common(grown_polymer)}"
    )
