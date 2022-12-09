""" Advent of Code - Day 7 """

file = open("input.txt", "r", encoding="utf-8")
lines = file.read().strip().split("\n")

cd = []
dirs = {}

for line in lines:
    cmd = line.split(" ")

    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "..":
                cd.pop()
            else:
                cd.append(cmd[2] + "/")
                dirs["".join(cd)] = 0
    elif cmd[0] != "dir":
        for index in range(len(cd)):
            dirs["".join(cd[: index + 1])] += int(cmd[0])

print(sum(s for s in dirs.values() if s <= 100000))

# Part two
FREE_SPACE = 70000000 - dirs["//"]
REQUIRED_SPACE = 30000000 - FREE_SPACE
print(min(size for size in dirs.values() if size >= REQUIRED_SPACE))
