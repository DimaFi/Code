suits = {
    1: "spades",
    2: "clubs",
    3: "diamonds",
    4: "hearts"
}

card_ranks = {
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "jack",
    12: "queen",
    13: "king",
    14: "ace"
}

m, k = map(int, input().split())

print(f"the {card_ranks[k]} of {suits[m]}")
