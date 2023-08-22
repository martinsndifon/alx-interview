#!/usr/bin/python3
"""ALX SE interview module"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    i = 0
    initial = sorted_coins[0]
    try:
        while True:
            if initial + sorted_coins[i] < total:
                count += 1
                initial += sorted_coins[i]
            elif initial == total:
                count += 1
                return count
            elif initial + sorted_coins[i] == total:
                count += 1
                return count
            elif initial + sorted_coins[i + 1] == total:
                count += 1
                return count
            else:
                i += 1
                count += 1
    except Exception as err:
        # print(err)
        return -1
