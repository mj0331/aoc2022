from pathlib import Path


class CaloriesCounter:
    def __init__(self) -> None:
        self.elf_calories = dict()

    def read_elf_calories_from_file(self, filepath: Path) -> None:
        with open(filepath, "r") as f:
            lines = f.readlines()

        elf_idx = 0

        for line in lines:
            if line == "\n":
                elf_idx += 1
                continue

            if elf_idx in self.elf_calories:
                self.elf_calories[elf_idx]["inventory"].append(int(line))
                self.elf_calories[elf_idx]["total_calories"] = sum(
                    self.elf_calories[elf_idx]["inventory"]
                )
            else:
                self.elf_calories[elf_idx] = {
                    "inventory": [int(line)],
                    "total_calories": int(line),
                }

    def count_elves(self) -> int:
        return len(self.elf_calories.keys())


if __name__ == "__main__":
    calories_counter = CaloriesCounter()
    calories_counter.read_elf_calories_from_file("input.txt")

    print(calories_counter.elf_calories)
    print(f"We have {calories_counter.count_elves()} elves accounted for.")

    # Challenge 1: Find the most calorific elf
    fattest_boi = max(calories_counter.elf_calories.items(), key=lambda elf: elf[1]['total_calories'])
    print(fattest_boi)

    # Challenge 2: Find the 3 most calorific elves and sum their calories
    calories = [elf['total_calories'] for _, elf in calories_counter.elf_calories.items()]
    calories.sort()
    print(sum(calories[-3:]))
    