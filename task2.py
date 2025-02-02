from functools import lru_cache

from visual_heatmap import visual_heatmap


def memo_dp(total, coins=None):

    coins = set(coins) if coins else [2, 3, 5, 6, 11, 13]

    @lru_cache(None)
    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")

        return min(helper(remaining - coin) + 1 for coin in coins)

    result = helper(total)
    return result if result != float("inf") else -1


def dp_min_coins(total, coins=None):
    coins = set(coins) if coins else [2, 3, 5, 6, 11, 13]

    dp = [float("inf")] * (total + 1)  # list with big numbers
    dp[0] = 0  # base case
    dp_states = []

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:

                dp[i] = min(dp[i], dp[i - coin] + 1)

        dp_states.append(dp.copy())
    # visual_heatmap(dp_states, total)

    return dp[total]
