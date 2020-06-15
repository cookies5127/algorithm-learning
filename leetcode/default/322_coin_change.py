import math
from typing import List


'''
322. Coin Change

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that
amount. If that amount of money cannot be made up by any combination of the coins,
return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
'''

EXAMPLES = [
    # (
    #     ([1, 2, 5], 11), 3,
    # ),
    # (
    #     ([2], 3), -1,
    # ),
    (
        ([186, 419, 83, 408], 6249), 20,
    ),
]


class Solution:

    def get_coins(self, coins: List[int], amount: int, memorize: dict) -> List[int]:
        if amount == 0:
            return []

        min_length = math.inf
        results = []
        for i, coin in enumerate(coins):
            if amount >= coin:
                max_count = amount // coin
                for count in range(max_count, 0, -1):
                    value = amount - count * coin
                    r = count * [coin]
                    if value in memorize:
                        r += memorize[value]
                    else:
                        temp = self.get_coins(coins[i:], value, memorize)
                        if sum(temp) == value:
                            r += temp
                            memorize[value] = temp
                        else:
                            memorize[value] = []

                    if sum(r) == amount and len(r) < min_length:
                        results = r
                        min_length = len(r)

        return results

    def coinChange(self, coins: List[int], amount: int) -> int:
        memorize = {c: [c] for c in coins}

        results = self.get_coins(coins, amount, memorize)
        return len(results) if sum(results) == amount else -1
