"""--- Day 6: Lanternfish ---
"""


def adjust_new_fishes_list(new_fishes: list, newborns: int) -> list:
    new_fishes[0] = new_fishes[1]
    new_fishes[1] = new_fishes[2]
    new_fishes[2] = newborns

    return new_fishes


def adjust_fishes_list(fishes, entering):
    tmp = fishes[0]
    for x in range(0, len(fishes) - 1):
        fishes[x] = fishes[x + 1]

    fishes[-1] = tmp + entering

    return fishes


def get_number_of_lanternfish(timers: list, days: int) -> int:
    fishes_per_day = [0] * 7
    for t in timers:
        fishes_per_day[t] += 1

    # tracks fishes 6, 7 and 8 days away from breeding
    # once a fish reaches 6, it is incorporated to the count in {fishes_per_day}
    new_fishes = [0] * 3

    for day in range(0, days):
        new_fishes = adjust_new_fishes_list(new_fishes, newborns=fishes_per_day[0])
        fishes_per_day = adjust_fishes_list(fishes_per_day, entering=new_fishes[0])

    return sum(fishes_per_day) + sum(new_fishes[1:])


if __name__ == "__main__":
    with open("input6.txt") as f:
        timers = list(map(int, f.readline().split(",")))

    print(f"The result for Part 1 is: {get_number_of_lanternfish(timers, days=80)}")
    print(f"The result for Part 2 is: {get_number_of_lanternfish(timers, days=256)}")
