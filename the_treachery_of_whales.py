"""--- Day 7: The Treachery of Whales ---
"""

import math
import statistics as stat


def find_fuel_cost_to_optimal_position(positions: list, optimal_position: int) -> list:
    """Finds the cost of moving to the optimal position for each possible submarine position

    Args:
        positions (list): [Position of each submarine]
        optimal_position (int): [Optimal movement destination]

    Returns:
        list: [Cost of moving to the optimal position for each possible submarine position]
    """
    # pos < optimal_position
    before_optimal = [0] * optimal_position

    counter = 1
    for i in range(len(before_optimal) - 1, -1, -1):
        before_optimal[i] += (
            counter if i + 1 == len(before_optimal) else counter + before_optimal[i + 1]
        )
        counter += 1

    # pos > optimal_position
    after_optimal = [0] * (max(positions) - optimal_position)
    counter = 1
    for i in range(0, len(after_optimal)):
        after_optimal[i] = counter if i == 0 else counter + after_optimal[i - 1]
        counter += 1

    return before_optimal + [0] + after_optimal


def find_fuel_expenditure(
    positions: list, optimal_position: tuple, constant_fuel: bool = True
) -> int:
    """Returns the amount of fuel needed by the submarines to reach the optimal position
    Two possible optimal positions are received. If they're the same, then the fuel
    expenditure is calculated once. If they are not, then fuel expenditure is calculated
    for each one, and the smallest one is returned.

    Args:
        positions (list): [Current position of each submarine]
        optimal_position (tuple): [Two possible optimal positions]
        constant_fuel (bool, optional): Indicates if fuel use is relative to distance. Defaults to True.

    Returns:
        int: [Fuel needed to reach the optimal position]
    """
    positions.sort()
    fuel_expenditure = [0, 0]

    if constant_fuel:
        for pos in positions:
            fuel_expenditure[0] += abs(optimal_position[0] - pos)

        if optimal_position[0] != optimal_position[1]:
            for pos in positions:
                fuel_expenditure[1] += abs(optimal_position[1] - pos)
        else:
            fuel_expenditure.pop(-1)

    else:
        fuel_costs = [
            find_fuel_cost_to_optimal_position(positions, optimal_position[0]),
            find_fuel_cost_to_optimal_position(positions, optimal_position[1]),
        ]
        for pos in positions:
            fuel_expenditure[0] += fuel_costs[0][pos]
            fuel_expenditure[1] += fuel_costs[1][pos]

    return min(fuel_expenditure)


def find_optimal_position(positions: list, constant_fuel: bool = True) -> tuple:
    """Finds two possible optimal position for the submarines

    Args:
        positions (list): [Current position of each submarine]
        constant_fuel (bool, optional): Indicates if fuel use is relative to distance. Defaults to True.

    Returns:
        tuple: [Two possible optimal positions for the submarines]
    """
    if constant_fuel:
        return (stat.median_low(positions), stat.median_high(positions))

    return (int(stat.mean(positions)), round(stat.mean(positions)))


def align_submarines(crab_positions: list, constant_fuel: bool = True) -> int:
    """Calls two methods, one for finding the optimal position for the submarines
    and the other one to calculate the fuel expenditure

    Args:
        crab_positions (list): [Current position of each submarine]
        constant_fuel (bool, optional): Indicates if fuel use is relative to distance. Defaults to True.

    Returns:
        int: [Total fuel needed to reach the optimal position]
    """
    optimal_position = find_optimal_position(crab_positions, constant_fuel)
    return find_fuel_expenditure(crab_positions, optimal_position, constant_fuel)


if __name__ == "__main__":
    with open("input7.txt", "r") as f:
        crab_positions = list(map(int, f.readline().split(",")))

    print(f"Solution for Part 1 of the problem is: {align_submarines(crab_positions)}")
    print(
        f"Solution for Part 2 of the problem is: {align_submarines(crab_positions, constant_fuel=False)}"
    )
