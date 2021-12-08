"""--- Day 8: Seven Segment Search ---
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Configuration:
    patterns: Dict[int, str] = field(default_factory=dict)
    segments: Dict[str, str] = field(
        default_factory=lambda: {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
            "g": None,
        }
    )
    output: list = field(default_factory=list)
    unidentified: list = field(default_factory=list)

    def decipher_patterns(self):
        # 1 - get 1, 4, 7, 8
        for u in self.unidentified:
            if len(u) == 2:
                self.patterns[1] = u
            elif len(u) == 3:
                self.patterns[7] = u
            elif len(u) == 4:
                self.patterns[4] = u
            elif len(u) == 7:
                self.patterns[8] = u

        # 2 - find a
        for l in self.patterns[7]:
            if l not in self.patterns[1]:
                self.segments["a"] = l

        # 3 - find 9
        proposed_9 = list(sorted(self.segments["a"] + "".join(self.patterns[4])))
        for u in self.unidentified:
            if len(u) == 6:
                if len(list(set(u) - set(proposed_9))) == 1:
                    self.patterns[9] = u
                    break

        # 4 - find g
        for l in self.patterns[9]:
            if l not in self.patterns[4] and l not in self.segments.values():
                self.segments["g"] = l

        # 5 - find 3
        for u in self.unidentified:
            if len(u) == 5:
                if self.patterns[1][0] in u and self.patterns[1][1] in u:
                    self.patterns[3] = u
                    # get d
                    temp_1 = self.patterns[1] + [self.segments["a"], self.segments["g"]]
                    d = list(set(self.patterns[3]) - set(temp_1))[0]
                    self.segments["d"] = d

        # 6 - perform cleaning
        for v in self.patterns.values():
            if v in self.unidentified:
                self.unidentified.remove(v)

        # 7 - find zero
        for u in self.unidentified:
            if len(u) == 6:
                if self.segments["d"] not in u:
                    self.patterns[0] = u
                else:
                    self.patterns[6] = u

        # 8 - find 2 and 5
        for u in self.unidentified:
            if len(u) == 5:
                if len(list(set(self.patterns[6]) - set(u))) == 2:
                    self.patterns[2] = u
                else:
                    self.patterns[5] = u

    def solve_problem_1(self):
        count = 0
        for p in self.patterns.values():
            if p in self.output:
                count += self.output.count(p)

        return count

    def solve_problem_2(self):
        ans = 0
        multiplier = 1000
        for o in self.output:
            for k, v in self.patterns.items():
                if v == o:
                    ans += k * multiplier

            multiplier //= 10

        return ans


def format_line(line: str) -> Configuration:
    pattern_str = line[:58]
    output_str = line[61:]
    unidentified = pattern_str.split()
    for u in range(len(unidentified)):
        unidentified[u] = list("".join(sorted(unidentified[u])))

    output = output_str.split()
    for o in range(len(output)):
        output[o] = list("".join(sorted(output[o])))

    configuration = Configuration(output=output, unidentified=unidentified)

    return configuration


if __name__ == "__main__":
    configurations = []
    with open("input8.txt", "r") as f:
        for line in f:
            configurations.append(format_line(line))

    counter_1_4_7_8 = 0
    for c in configurations:
        c.decipher_patterns()
        counter_1_4_7_8 += c.solve_problem_1()

    print(counter_1_4_7_8)

    sum_ = 0
    for c in configurations:
        sum_ += c.solve_problem_2()

    print(sum_)
