""" Advent of Code - Day 5 """


def parse_stacks(stacks_raw):
    """Returns the list containing stacks after parsing raw input"""
    lines = stacks_raw.split("\n")

    MAX_STACKS = int(lines[-1][-1])

    stacks_list = [[] for i in range(MAX_STACKS)]

    for line in lines:
        for index, character in enumerate(line):
            if character.isalpha():
                list_number = int(lines[-1][index])
                stacks_list[list_number - 1].insert(0, character)

    return stacks_list


def parse_instructions(steps):
    """Returns the num of crates, source stack and destination stack from the given raw step"""
    num_crates, source_stack, destination_stack = [
        element for element in steps.split(" ") if element.isdigit()
    ]

    return int(num_crates), int(source_stack), int(destination_stack)


file = open("input.txt", "r", encoding="utf-8")

stack_raw, steps_raw = file.read().split("\n\n")

stacks = parse_stacks(stack_raw)

steps_lines = steps_raw.split("\n")
for step in steps_lines:

    quantity, source, destination = parse_instructions(step)

    aux = []
    for i in range(quantity):
        crate = stacks[source - 1].pop()
        aux.append(crate)

    # For part two
    for letter in reversed(aux):
        stacks[destination - 1].append(letter)

for stack in stacks:
    print(stack[-1])

file.close()
