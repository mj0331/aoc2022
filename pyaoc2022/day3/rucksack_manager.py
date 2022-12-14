from pathlib import Path


ITEM_PRIORITY_LIST = list("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def read_rucksack_data(path: Path) -> list:
    with open(path, "r") as f:
        return [parse_rucksack_data(line.strip()) for line in f.readlines()]


def item_str_to_priority(item: str) -> int:
    assert (
        l := len(item)
    ) == 1, f"Item string must be 1 character, not {l} for priority calculation!"

    return ITEM_PRIORITY_LIST.index(item)


def parse_rucksack_data(line: str, containers: int = 2) -> dict:
    rucksack_data = {"line": line, "containers": [], "common_parts": []}

    # Split rucksack content in containers
    container_size, spillover = divmod(len(line), containers)

    # Panic if the desired container size is larger than the current rucksack
    assert (
        container_size > 0
    ), f"Cannot divide rucksack of size {len(line)} in more containers ({containers}) than the length of the rucksack!"

    rucksack_data["containers"] = [
        line[i * container_size : min(len(line), (i + 1) * container_size)]
        for i in range(containers)
    ]

    # Add the remaining spillover to the last container
    if spillover > 0:
        rucksack_data["containers"][-1] += line[-spillover:]

    # Find the common parts between all containers
    # Track which part appears in which containers
    parts_counter = {}

    for i in range(len(line)):
        part = line[i]

        if part in parts_counter:
            parts_counter[part].append(i // container_size)
        else:
            parts_counter[part] = [i // container_size]

    # Handle the case where a part appears multiple times in the same container
    # Now we can also figure out which part appears in all containers
    for key in parts_counter:
        parts_counter[key] = set(parts_counter[key])

        if len(parts_counter[key]) == containers:
            rucksack_data["common_parts"].append(key)

    return rucksack_data


if __name__ == "__main__":
    # Challenge 1: Sum of the priorities of all common parts
    rucksack_data = read_rucksack_data("rucksacks.txt")

    common_part_priority_sum = sum(
        [
            sum([item_str_to_priority(part) for part in rucksack["common_parts"]])
            for rucksack in rucksack_data
        ]
    )

    print(f"Sum of priorities of all common parts is {common_part_priority_sum}")

    # Challenge 2: Sum of the priorities of the common part between elf groups of 3 elves each
    # I wanted to try something clever here. It didn't work, so have a naive solution.

    challenge_2_sum = 0
    group_size = 3

    for i in range(0, len(rucksack_data), group_size):
        parts_counter = {}

        for j in range(group_size):
            line = rucksack_data[i + j]['line']
            line_length = len(line)

            for k in range(line_length):
                part = line[k]

                if part in parts_counter:
                    parts_counter[part].append(i + j)
                else:
                    parts_counter[part] = [i + j]

        for key in parts_counter:
            parts_counter[key] = set(parts_counter[key])

            if len(parts_counter[key]) == group_size:
                challenge_2_sum += item_str_to_priority(key)

    print(f"Sum of badge priorities of all elf groups is {challenge_2_sum}")
