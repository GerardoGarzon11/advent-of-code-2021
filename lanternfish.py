"""--- Day 6: Lanternfish ---
"""

from dataclasses import dataclass


@dataclass
class Lanternfish:
    """Represents a lanternfish and its internal cycles"""

    newborn: bool = True
    timer: int = 8

    def adjust_timer(self):
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            self.newborn = False

    def create_new_lanternfish(self):
        if self.timer == 6 and not self.newborn:
            return True

        return False


def get_number_of_lanternfish(timers: list, days: int) -> int:
    """Returns the number of lanternfish after {days}

    Args:
        timers (list): [Timers for each lanternfish]
        days (int): [Number of days]

    Returns:
        int: [Final number of lanternfish]
    """
    fishes = []
    for t in timers:
        fishes.append(Lanternfish(newborn=False, timer=t))

    new_fishes = []
    for day in range(0, days):
        fishes += new_fishes
        new_fishes.clear()
        for fish in fishes:
            fish.adjust_timer()

            if fish.create_new_lanternfish():
                new_fishes.append(Lanternfish())

    fishes += new_fishes

    return len(fishes)


if __name__ == "__main__":
    with open("input6_test.txt") as f:
        timers = list(map(int, f.readline().split(",")))

    print(f"The result for Part 1 is: {get_number_of_lanternfish(timers, days=80)}")
