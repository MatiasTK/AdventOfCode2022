""" Advent of Code - Day 4 """


def is_id_contained(first_id, second_id):
    """Convert the IDS to sets and returns if one is subset of the other"""
    first_set = set(first_id)
    second_set = set(second_id)

    return first_set.issubset(second_set) or second_set.issubset(first_set)


def is_id_overlap(first_id, second_id):
    """Returns true if the numbers in one of the ids overlaps the other"""
    for num in first_id:
        if num in second_id:
            return True

    return False


def generate_ids(pair_str: str):
    """Generates two list with the complete id range of the pair"""
    first, second = pair_str.split(",")

    first_id = []
    second_id = []

    first_start, first_end = map(int, first.split("-"))
    second_start, second_end = map(int, second.split("-"))

    for num in range(first_start, first_end + 1):
        first_id.append(num)
    for num in range(second_start, second_end + 1):
        second_id.append(num)
    return first_id, second_id


file = open("input.txt", "r", encoding="utf-8")

pairs = file.read().split("\n")

total_id_contained = 0
total_id_overlapped = 0

for pair in pairs:
    i1, i2 = generate_ids(pair)
    if is_id_contained(i1, i2):
        total_id_contained += 1
    if is_id_overlap(i1, i2):
        total_id_overlapped += 1

print("The total pairs that fully contain the others are", total_id_contained)
print("The total pairs that are overlapped are", total_id_overlapped)

file.close()
