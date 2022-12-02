""" Advent of Code - Day 1"""
file = open("input.txt", "r", encoding="utf-8")


def find_top(elves_list: list):
    """Returns the top 3 elves carrying most calories"""
    sums = []

    for elf_item in elves_list:
        total_calories = 0
        for calorie in elf_item:
            total_calories += calorie

        sums.append(total_calories)

    sums.sort(reverse=True)

    return [sums[0], sums[1], sums[2]]


split = file.read().split("\n")
elves = []

elf = []
for e in split:
    if e == "":
        elves.append(elf)
        elf = []
    else:
        elf.append(int(e))

top = find_top(elves)
total_top = sum(top)

print("The elf carrying most calories is carrying", top[0])
print("The top three elves are carrying in total", total_top)

file.close()
