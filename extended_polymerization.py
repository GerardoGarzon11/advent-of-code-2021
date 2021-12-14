"""--- Day 14: Extended Polymerization ---
"""


def parseData():
    with open("input14.txt") as f:
        template, raw_rules = f.read().split("\n\n")
        rules = {}
        for r in raw_rules.splitlines():
            split = r.split(" -> ")
            rules[split[0]] = split[1]

    return (template, rules)


def grow_polymer(template: str, rules: dict, steps: int = 10) -> str:
    for x in range(steps):
        new = ""
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            if not new:
                new = pair[0]

            new += rules[pair] + pair[1]

        template = new

    return template


def get_difference_between_most_common_and_least_common(polymer: str) -> int:
    elements = set(polymer)
    most_common, least_common = -1, -1
    for e in elements:
        element_count = polymer.count(e)
        if element_count > most_common:
            most_common = element_count
        if element_count < least_common or least_common == -1:
            least_common = element_count

    return most_common - least_common


if __name__ == "__main__":
    parseData = parseData()
    template = parseData[0]
    rules = parseData[1]

    grown_polymer = grow_polymer(template, rules)

    print(
        f"The difference between the quantity of the most common element and the quantity of the least common element is: {get_difference_between_most_common_and_least_common(grown_polymer)}"
    )

    grown_polymer = grow_polymer(grown_polymer, rules, steps=30)

    print(
        f"The difference after 40 steps is: {get_difference_between_most_common_and_least_common(grown_polymer)}"
    )
