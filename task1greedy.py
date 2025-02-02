def greedy(total: int, coins=None):
    coins = set(coins) if coins else [2, 3, 5, 6, 11, 13]

    di = {i: 0 for i in coins}
    qty = 0
    for i in coins:
        if total // i > 0:
            di[i] = total // i
            qty += di[i]
            total = total - (di[i] * i)
    return (di, qty)
