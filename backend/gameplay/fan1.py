def all_chow(hand):
    for combo in hand:
        return all(b - a == 1 for a, b in zip(combo, combo[1:]))