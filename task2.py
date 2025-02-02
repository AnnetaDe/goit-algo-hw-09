# Функція жадібного алгоритму find_coins_greedy.
# Ця функція повинна приймати суму, яку потрібно видати покупцеві,
# і повертати словник із кількістю монет кожного номіналу,
# що використовуються для формування цієї суми.
# Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}.
# Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.


def greedy(total: int):
    coins = [50, 20, 10, 5, 2, 1]
    di = {i: 0 for i in coins}
    qty = 0
    for i in coins:
        if total // i > 0:
            di[i] = total // i
            qty += di[i]
            total = total - (di[i] * i)
    return (di, qty)


total = int(
    input(
        "Enter the amount you want to get \n from the collection of coins |50| |20| |10| |5| |2| |1| "
    )
)
print(f"Total coins -- {greedy(total)[1]}")
for key, value in greedy(total)[0].items():
    print(f"coin value *** {key} *** quantity of coins - {value}")
