#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make
    change for a given total amountself.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target total amount to make change forself.

    Returns:
        int: The minimum number of coins needed to achieve the target total.
        Returns -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
