""" Advent of code - Day 9 """


def move_tail(head_pos_x, head_pos_y, tail_pos_x, tail_pos_y):
    """Returns the new X and Y coordinates of the tail"""
    if head_pos_x - 2 == tail_pos_x and head_pos_y == tail_pos_y:
        tail_pos_x += 1

    elif head_pos_x + 2 == tail_pos_x and head_pos_y == tail_pos_y:
        tail_pos_x -= 1

    elif head_pos_x == tail_pos_x and head_pos_y - 2 == tail_pos_y:
        tail_pos_y += 1

    elif head_pos_x == tail_pos_x and head_pos_y + 2 == tail_pos_y:
        tail_pos_y -= 1

    elif head_pos_x - 1 == tail_pos_x and head_pos_y - 2 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y += 1

    elif head_pos_x + 1 == tail_pos_x and head_pos_y - 2 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y += 1

    elif head_pos_x + 1 == tail_pos_x and head_pos_y + 2 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y -= 1

    elif head_pos_x - 1 == tail_pos_x and head_pos_y + 2 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y -= 1

    elif head_pos_x + 2 == tail_pos_x and head_pos_y - 1 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y += 1

    elif head_pos_x + 2 == tail_pos_x and head_pos_y + 1 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y -= 1

    elif head_pos_x - 2 == tail_pos_x and head_pos_y + 1 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y -= 1

    elif head_pos_x - 2 == tail_pos_x and head_pos_y - 1 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y += 1

    elif head_pos_x - 2 == tail_pos_x and head_pos_y - 2 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y += 1

    elif head_pos_x + 2 == tail_pos_x and head_pos_y + 2 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y -= 1

    elif head_pos_x - 2 == tail_pos_x and head_pos_y + 2 == tail_pos_y:
        tail_pos_x += 1
        tail_pos_y -= 1

    elif head_pos_x + 2 == tail_pos_x and head_pos_y - 2 == tail_pos_y:
        tail_pos_x -= 1
        tail_pos_y += 1

    return tail_pos_x, tail_pos_y


file = open("input.txt", "r", encoding="utf-8")

lines = file.read().split("\n")

head_x = 0
head_y = 0

tail_x = 0
tail_y = 0

tail_visits = []

# Part one
for line in lines:
    direction, distance = line.split(" ")

    for j in range(int(distance)):
        if direction == "R":
            head_x += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "U":
            head_y += 1
        elif direction == "D":
            head_y -= 1

        tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
        tail_visits.append([tail_x, tail_y])
print(len(set(tuple(i) for i in tail_visits)))

head_x = 0
head_y = 0

tails = [[0, 0]] * 9
tail_visits = []


# Part two
for line in lines:
    direction, distance = line.split(" ")

    for i in range(int(distance)):
        if direction == "R":
            head_x += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "U":
            head_y += 1
        elif direction == "D":
            head_y -= 1

        for j, tail in enumerate(tails):
            current_tail_x = tails[j][0]
            current_tail_y = tails[j][1]

            if j == 0:
                current_tail_x, current_tail_y = move_tail(
                    head_x, head_y, current_tail_x, current_tail_y
                )
            else:
                current_tail_x, current_tail_y = move_tail(
                    tails[j - 1][0], tails[j - 1][1], current_tail_x, current_tail_y
                )

            tails[j] = [current_tail_x, current_tail_y]

            if j == 8:  # Last tail
                tail_visits.append([current_tail_x, current_tail_y])

print(len(set(tuple(i) for i in tail_visits)))
