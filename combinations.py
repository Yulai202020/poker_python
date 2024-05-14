nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
nums.reverse()


def power_of(card):
    if type(card) == list:
        return nums.index(card[1])+2
    else:
        return nums.index(card[1:])+2

def is_flush(hand, desk):
    a = desk + hand
    g1 = [i[0] for i in a]

    g3 = ''
    for i in g1:
        g3 += i

    from collections import Counter

    def most_common_element(arr):
        counter = Counter(arr)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else None

    most_common = most_common_element(g3)

    if len(set([i[0] for i in a])) < 4:
        ids = []
        for i in range(7):
            if a[i][0] == most_common:
                ids.append(i)

        if 5 in ids and 6 not in ids:
            return (True, power_of[hand[0]])

        elif 6 in ids and 5 not in ids:
            return (True, power_of(hand[1]))

        elif 5 in ids and 6 in ids:
            g = [power_of(hand[0]), power_of(hand[1])]
            return (True, g)

        elif 5 not in ids and 6 not in ids:
            return (False, None)

    else:
        return (False, None)
