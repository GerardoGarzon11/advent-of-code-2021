"""--- Day 3: Binary Diagnostic ---
"""


def count_bits_in_report(report):
    """Returns the count of 0's and 1's for each column in the report

    Args:
        report ([list]): [List of binary numbers]

    Returns:
        [list]: [A list containing two lists, one counting 0's per position, the other
        count 1's per position]
    """
    bit_counts = [[0] * len(report[0]), [0] * len(report[0])]

    for line in report:
        for bit in range(0, len(line)):
            if line[bit] == "1":
                bit_counts[1][bit] += 1
            else:
                bit_counts[0][bit] += 1

    return bit_counts


def get_power_consumption(report):
    """Calculates gamma_rate and epsilon_rate, then uses them to calculate the power consumption

    Args:
        report ([list]): [A list of binary strings representing the diagnostic]

    Returns:
        [int]: [Power consumption of the submarine]
    """
    bit_counts = count_bits_in_report(report)
    num_report_lines = len(report)

    # Calculate gamma and epsilon rates
    gamma_rate, epsilon_rate = "", ""
    for col_count in bit_counts[1]:
        if col_count > num_report_lines / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    # Power consumption
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    return power_consumption


def get_life_support_rating(report: list):
    """Calculates Oxygen Generator Rating and the calculates CO2 Scrubber Rating,
     then uses these values to obtain the Life Support Rating

    Args:
        report (list): [A list of binary strings representing the diagnostic]

    Returns:
        [int]: [Life Support Rating of the submarine]
    """
    # ogr_found - boolean, has the Oxygen Generator Rating been found?
    # csr_found - boolean, has the CO2 Scrubber Rating been found?
    ogr_found, csr_found = False, False

    # Each one gets its copy of the report
    oxygen_report, co2_report = report.copy(), report.copy()
    ogr_rating, co2_rating = None, None
    oxygen_col, co2_col = 0, 0

    while not ogr_found or not csr_found:
        if not ogr_found:
            oxygen_count = count_bits_in_report(oxygen_report)

            oxygen_most_common_bit = (
                "0"
                if oxygen_count[0][oxygen_col] > oxygen_count[1][oxygen_col]
                else "1"
            )

            # filter lines that contain [oxygen_most_common_bit] in column number [oxygen_col]
            tmp_oxygen_report = oxygen_report.copy()
            for line in tmp_oxygen_report:
                if line[oxygen_col] != oxygen_most_common_bit:
                    oxygen_report.remove(line)

            if len(oxygen_report) == 1:
                ogr_rating = oxygen_report[0]
                ogr_found = True

            oxygen_col += 1

        if not csr_found:
            co2_count = count_bits_in_report(co2_report)

            co2_least_common_bit = (
                "0" if co2_count[0][co2_col] <= co2_count[1][co2_col] else "1"
            )

            # filter lines that contain [co2_least_common_bit] in column number [co2_col]
            tmp_co2_report = co2_report.copy()
            for line in tmp_co2_report:
                if line[co2_col] != co2_least_common_bit:
                    co2_report.remove(line)

            if len(co2_report) == 1:
                co2_rating = co2_report[0]
                csr_found = True

            co2_col += 1

    decimal_ogr_rating = int(ogr_rating, 2)
    decimal_csr_rating = int(co2_rating, 2)
    life_support_rating = decimal_ogr_rating * decimal_csr_rating

    return life_support_rating


if __name__ == "__main__":
    input = []
    with open("input3.txt", "r") as f:
        for line in f:
            input.append(line.strip())

    print(f"The power consumption is {get_power_consumption(input)}")
    print(f"The life support rating is {get_life_support_rating(input)}")
