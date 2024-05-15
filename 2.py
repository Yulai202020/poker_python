from combinations import *
from player import Player
import random

nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
nums.reverse()

def sort_cards(cards):
    result = []
    for i in range(len(cards)):
        result.append([cards[i][0], cards[i][1:]])
    return result

def print_card(card, end="\n"):
    if card[0] == "d":
        print("♦" + card[1], end=end)
    elif card[0] == "h":
        print("♥" + card[1], end=end)
    elif card[0] == "s":
        print("♠" + card[1], end=end)
    elif card[0] == "c":
        print("♣" + card[1], end=end)
    else:
        pass

def create_colode(gone):
    result = []
    for i in nums:
        if 'd' + i not in gone: # diamond
            result.append('d' + i)
        if 'c' + i not in gone: # clubs
            result.append('c' + i)
        if 's' + i not in gone: # spades
            result.append('s' + i)
        if 'h' + i not in gone: # hearts
            result.append('h' + i)

    return result

gone = []
colode = create_colode(gone)
desk = []

a = []
count_of_players = int(input("Enter count of players: "))

for i in range(count_of_players):
    i1 = random.randint(0,len(colode)-1)
    i2 = random.randint(0,len(colode)-1)

    gone.append(colode[i1])
    gone.append(colode[i2])

    my_hand_list = sort_cards([colode[i1], colode[i2]])

    colode = create_colode(gone)

    a.append(my_hand_list)

# create desk
for i in range(5):
    i1 = random.randint(0, len(colode)-1)

    gone.append(colode[i1])
    desk.append(colode[i1])

    colode = create_colode(gone)

desk = sort_cards(desk)

# print cards of players
print("\nPlayers cards")
for i in a:
    print_card(i[0], end=" ")
    print_card(i[1], end=" ")
    print()

# print cards on desk
print("\nCards on desk")
for i in desk:
    print_card(i, end=" ")

print("\n")

# know who won
b = {}

for i in range(len(a)):
    if is_flush_royal(a[i], desk)[0]:
        b[i] = [5, is_flush_royal(a[i], desk)[1]]

    elif is_quards(a[i], desk)[0]:
        b[i] = [4, is_quards(a[i], desk)[1]]

    elif is_flush(a[i], desk)[0]:
        b[i] = [3, is_flush(a[i], desk)[1]]

    elif is_set(a[i], desk)[0]:
        b[i] = [2, is_set(a[i], desk)[1]]

    elif is_one_pair(a[i], desk)[0]:
        b[i] = [1, is_one_pair(a[i], desk)[1]]

    else:
        abc = []
        abc.append(power_of(a[i][0]))
        abc.append(power_of(a[i][1]))
        b[i] = [0, max(abc)]

values = [value[0] for key, value in b.items()]
maximum = max(values)
ids = [i for i, j in enumerate(values) if j == maximum]

if len(ids) == 1:
    print(f"player {ids[0]+1} won !")
else:
    pass