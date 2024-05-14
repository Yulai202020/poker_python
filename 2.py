from combinations import *
from player import Player

def sort_cards(cards):
    result = []
    for i in range(len(cards)):
        result.append([cards[i][0], cards[i][1:]])
    return result

hand1 = sort_cards(["hK", "h9"])
desk = sort_cards(["p6", "d10", "pK", "pQ", "h10"])
hand2 = sort_cards(["p3", "p7"])

if is_flush(hand1, desk)[0] and not is_flush(hand2, desk)[0]:
    print("player 1 won")

elif is_flush(hand2, desk)[0] and not is_flush(hand1, desk)[0]:
    print("player 2 won")

elif  is_flush(hand1, desk)[0] == True and is_flush(hand2, desk)[0] == True:
    if is_flush(hand1, desk)[1] > is_flush(hand2, desk)[0]:
        print("player 1 won")
    elif is_flush(hand1, desk)[1] < is_flush(hand2, desk)[0]:
        print("player 2 won")
    else:
        print("draw")

else:
    first = [power_of(hand1[0]), power_of(hand1[1])]
    second = [power_of(hand2[0]), power_of(hand2[1])]
    first_max = max(first)
    second_max = max(second)

    if first_max > second_max:
        print("player 1 won")
    elif first_max < second_max:
        print("player 2 won")
    else:
        print("draw")
