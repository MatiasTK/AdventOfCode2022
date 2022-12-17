""" Advent of Code - Day 10 """

file = open(
    "input.txt",
    "r",
    encoding="utf-8",
)


def add_cycle_values(cycle, x_current_value, cycles_list):
    if cycle == 20:
        cycles_list.append(x_current_value * 20)
    elif cycle == 60:
        cycles_list.append(x_current_value * 60)
    elif cycle == 100:
        cycles_list.append(x_current_value * 100)
    elif cycle == 140:
        cycles_list.append(x_current_value * 140)
    elif cycle == 180:
        cycles_list.append(x_current_value * 180)
    elif cycle == 220:
        cycles_list.append(x_current_value * 220)


lines = file.read().strip().split("\n")

x_value = 1
cycle_number = 0

cycles_values = []
waiting_to_add, next_to_add = False, 0

for line in lines:
    instruction = line.split(" ")

    cycle_number += 1

    add_cycle_values(cycle_number, x_value, cycles_values)

    if waiting_to_add:
        cycle_number += 1
        x_value += next_to_add
        add_cycle_values(cycle_number, x_value, cycles_values)

    if instruction[0] == "addx":
        waiting_to_add = True
        next_to_add = int(instruction[1])
    elif instruction[0] == "noop":
        waiting_to_add = False

print(sum(cycles_values))

# Part two

sprite_position = 0
crt_position = -1
x_value = 1
draw = ""
for line in lines:
    instruction = line.split(" ")

    if instruction[0] == "addx":
        crt_position += 1
        if crt_position % 40 == 0:
            draw += "\n"
            crt_position = 0
        if sprite_position - 1 <= crt_position <= sprite_position + 1:
            draw += "#"
        else:
            draw += "."

        crt_position += 1
        if crt_position % 40 == 0:
            draw += "\n"
            crt_position = 0
        if sprite_position - 1 <= crt_position <= sprite_position + 1:
            draw += "#"
        else:
            draw += "."
        x_value += int(instruction[1])
        sprite_position = x_value
    else:
        crt_position += 1
        if crt_position % 40 == 0:
            draw += "\n"
            crt_position = 0
        if sprite_position - 1 <= crt_position <= sprite_position + 1:
            draw += "#"
        else:
            draw += "."


print(draw)

file.close()
