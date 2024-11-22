# Add header later



import string

def change(coins, amount ):
    """Calculate minimal change for a given amount of money with given coins"""
    A = [None] * (amount + 1)
    A[0] = [] # Empty list
    for i in range(1, amount + 1):
        for denom in coins:
            if ((i >= denom) and (A[i - denom] is not None)):
                candidate = A[i - denom] + [denom]
                if ((A[i] is None) or (len(candidate) < len(A[i]))):
                    # This candidate is better than the current best, so replace
                    A[i] = candidate
    
    return A[amount]
# End of change() function


if (__name__ == "__main__"):
    coins = [1, 2, 5]
    amount = 11
    coins_returned = change(coins, amount)
    no_of_coins = len(coins_returned)
    print("Min number of coins needed to return change for", amount, "=", no_of_coins)
    print("Combination of coins returned:", coins_returned)