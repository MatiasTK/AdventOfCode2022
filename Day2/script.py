""" Advent of Code - Day 2 """
results = {"win": 6, "lose": 0, "tie": 3}

points = {
    # Rock
    "X": {"point": 1, "A": results["tie"], "B": results["lose"], "C": results["win"]},
    # Paper
    "Y": {"point": 2, "A": results["win"], "B": results["tie"], "C": results["lose"]},
    # Scissors
    "Z": {"point": 3, "A": results["lose"], "B": results["win"], "C": results["tie"]},
}


def apply_strategy(player_char: str, opponent_char: str):
    """Returns the new player character after applying the strategy"""
    if player_char == "X":
        for play, play_property in points.items():
            if play_property[opponent_char] == results["lose"]:
                return play
    elif player_char == "Y":
        for play, play_property in points.items():
            if play_property[opponent_char] == results["tie"]:
                return play
    elif player_char == "Z":
        for play, play_property in points.items():
            if play_property[opponent_char] == results["win"]:
                return play


file = open("input.txt", "r", encoding="utf-8")

parsed_data = file.read().split("\n")

total_score = 0
total_score_with_strategy = 0

for index, value in enumerate(parsed_data):
    opponent = parsed_data[index][0]
    player = parsed_data[index][2]

    total_score += points[player]["point"] + points[player][opponent]

    new_player = apply_strategy(player, opponent)

    total_score_with_strategy += (
        points[new_player]["point"] + points[new_player][opponent]
    )


print("The total score without any strategy is", total_score)
print("The total score according to the strategy is", total_score_with_strategy)

file.close()
