# CPSC 335
# Project 3
# Problem 1

# Group Members:
# Kshitij Pingle
# John Carlo Manuel
# Timothy Tran


def change(coins : list, amount : int) -> tuple:
    """Calculate minimal change for a given amount of money with given coins"""
    num_of_coins = 0
    A = [None] * (amount + 1)   # Initialize list of lists
    A[0] = []                   # Base case: no coins needed for 0 amount
    for i in range(1, amount + 1):
        for denom in coins:
            # Check for every coin denomination
            if ((i >= denom) and (A[i - denom] is not None)):
                candidate = A[i - denom] + [denom]
                if ((A[i] is None) or (len(candidate) < len(A[i]))):
                    # This candidate is better than the current best, so replace
                    A[i] = candidate
    if (A[amount] is None):
        num_of_coins = -1
    else:
        num_of_coins = len(A[amount])

    return (num_of_coins, A[amount])
# End of change() function


if (__name__ == "__main__"):
    coins = [1, 2, 5]
    amount = 11
    no_of_coins, coins_returned = change(coins, amount)
    print("Minimum number of coins needed to return change for", amount, "=", no_of_coins)
    print("Combination of coins returned :", coins_returned)
