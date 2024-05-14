nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
nums.reverse()

def power_of(card):
    if type(card) == list:
        return nums.index(card[1])+2
    else:
        return nums.index(card[1:])+2

def is_flush_royal(hand, desk):
    a = desk + hand

    suits_str = ''
    for i in suits:
        suits_str += i

    from collections import Counter

    def most_common_element(arr):
        counter = Counter(arr)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else None

    flush_suit = most_common_element(suits_str)

    if is_flush(hand, desk)[0]:
        g1 = [flush_suit + "A", flush_suit + "K", flush_suit + "Q", flush_suit + "J", flush_suit + "10"]
        g = g1 in a
        if g:
            if a[5] in g1:
                return (True, power_of(hand[0]))
            elif a[6] in g1:
                return (True, power_of(hand[1]))
            elif a[5] in g1 and a[6] in g1:
                g = max([power_of(hand[0]), power_of(hand[1])])
                return (True, g)
            elif a[5] not in g1 and a[6] not in g1:
                return (False, None)
        else:
            return (False, None)

def is_flush(hand, desk):
    a = desk + hand
    suits = [i[0] for i in a]

    suits_str = ''
    for i in suits:
        suits_str += i

    from collections import Counter

    def most_common_element(arr):
        counter = Counter(arr)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else None

    flush_suit = most_common_element(suits_str)

    if len(set([i[0] for i in a])) < 4:
        ids = []
        for i in range(7):
            if a[i][0] == flush_suit:
                ids.append(i)

        if 5 in ids and 6 not in ids:
            return (True, power_of[hand[0]])

        elif 6 in ids and 5 not in ids:
            return (True, power_of(hand[1]))

        elif 5 in ids and 6 in ids:
            g = max([power_of(hand[0]), power_of(hand[1])])
            return (True, g)

        elif 5 not in ids and 6 not in ids:
            return (False, None)

    else:
        return (False, None)
