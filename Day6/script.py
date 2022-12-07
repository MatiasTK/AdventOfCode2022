""" Advent of Code - Day 6 """
file = open("input.txt", "r", encoding="utf-8")

data = file.read()


def find_start_of_packet(datastream, distinct_characters):
    """Returns how many characters needs to be processed before the first
    start-of-message marked is detected with the given distinct_characters"""
    packet_start = 0
    packet_end = len(datastream)

    while packet_start < packet_end:
        word = ""

        if packet_start + distinct_characters > packet_end:
            return -1  # NOT FOUND

        for index in range(packet_start, packet_start + distinct_characters):
            word += datastream[index]

        packet_start += 1

        if len(set(word)) == distinct_characters:
            return packet_start + (distinct_characters - 1)


# Part one
print(
    find_start_of_packet(data, 4),
    "packages needs to be processed with 4 distinct characters",
)

# Part two
print(
    find_start_of_packet(data, 14),
    "packages needs to be processed with 14 distinct characters",
)

file.close()
