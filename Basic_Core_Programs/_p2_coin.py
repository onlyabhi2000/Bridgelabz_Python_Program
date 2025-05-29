import random


def flip_coin(n):
    heads = 0
    tails = 0

    for i in range(n):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    head_percent = (heads / n) * 100
    tail_percent = (tails / n) * 100

    print(f"Heads: {heads} ({head_percent:.2f}%)")
    print(f"Tails: {tails} ({tail_percent:.2f}%)")


flips = int(input("Enter number of times to flip the coin: "))
if flips <= 0:
    print("Please enter a positive integer")
else:
    flip_coin(flips)
