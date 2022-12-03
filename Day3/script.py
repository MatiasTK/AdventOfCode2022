""" Advent of Code - Day 3 """


def find_rucksack_letter(rucksack_list: list):
    """Returns the letter which appears on two compartments"""
    rucksack_middle = len(rucksack_list) // 2
    first_half = rucksack_list[:rucksack_middle]
    second_half = rucksack_list[rucksack_middle:]

    for letter in first_half:
        if letter in second_half:
            return letter


def find_priority(letter: str):
    """Returns the priority number of the given letter"""
    toInt = ord(letter)

    if letter.islower():
        return toInt - 96
    else:
        return toInt - 38


def find_rucksacks_badge(rucksacks_list: list):
    """Returns the letter which appears on 3 rucksacks given"""
    first_rucksack = rucksacks_list[0]
    second_rucksack = rucksacks_list[1]
    third_rucksack = rucksacks_list[2]

    for letter in first_rucksack:
        if letter in second_rucksack and letter in third_rucksack:
            return letter


file = open("input.txt", "r", encoding="utf-8")

rucksacks = file.read().split("\n")

priority_sum = 0

# First Part
for rucksack in rucksacks:
    priority_letter = find_rucksack_letter(rucksack)
    priority_sum += find_priority(priority_letter)

print("The sum of the priorities are:", priority_sum)

priority_sum = 0

# Second Part
elves_rucksack = []
for index, rucksack in enumerate(rucksacks):
    elves_rucksack.append(rucksack)
    if (index + 1) % 3 == 0:
        priority_letter = find_rucksacks_badge(elves_rucksack)
        priority_sum += find_priority(priority_letter)
        elves_rucksack = []

print("The sum of priorities of each three-Elf group are:", priority_sum)

file.close()
