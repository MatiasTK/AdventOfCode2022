""" Advent of Code - Day 11 """

file = open("input.txt", "r", encoding="utf-8")

data = file.read().strip().split("\n\n")

monkeys = [
    {
        "items": [],
        "operations": "",
        "test": 0,
        "test_true": 0,
        "test_false": 0,
        "inspected_times": 0,
    }
    for i in range(len(data))
]

mod = 1

for d in data:
    monkey_lines = d.split("\n")

    monkey_id = int(monkey_lines[0].split(" ")[1][0])

    monkeys[monkey_id]["items"] = monkey_lines[1].split(":")[1].strip().split(",")
    monkeys[monkey_id]["operations"] = monkey_lines[2].split("=")[1].strip()
    monkeys[monkey_id]["test"] = int(monkey_lines[3].split(" ")[-1].strip())
    monkeys[monkey_id]["test_true"] = int(monkey_lines[4].split(" ")[-1])
    monkeys[monkey_id]["test_false"] = int(monkey_lines[5].split(" ")[-1])


for m in monkeys:
    mod *= m["test"]

for i in range(1000):
    for monkey in monkeys:
        for item in monkey["items"]:
            modulo = 1

            worry_level = int(item)
            operation = monkey["operations"].split(" ")

            p1 = 0
            p2 = 0

            if operation[0] == "old":
                p1 = int(item)
            elif operation[0].isdigit():
                p1 = int(operation[0])

            if operation[2] == "old":
                p2 = int(item)
            elif operation[2].isdigit():
                p2 = int(operation[2])

            if operation[1] == "*":
                worry_level = p1 * p2
            elif operation[1] == "+":
                worry_level = p1 + p2

            # worry_level //= 3

            worry_level = worry_level % mod

            if worry_level % monkey["test"] == 0:
                if item in monkey["items"]:
                    monkey["items"] = list(filter(lambda x: x != item, monkey["items"]))
                monkeys[monkey["test_true"]]["items"].append(worry_level)
            else:
                if item in monkey["items"]:
                    monkey["items"] = list(filter(lambda x: x != item, monkey["items"]))
                monkeys[monkey["test_false"]]["items"].append(worry_level)

            monkey["inspected_times"] += 1

monkeys.sort(key=lambda x: x["inspected_times"], reverse=True)
print(monkeys[0]["inspected_times"] * monkeys[1]["inspected_times"])


file.close()
