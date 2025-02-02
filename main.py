from my_timer import time_it
from task2 import dp_min_coins, memo_dp
from task1greedy import greedy


foo_to_compare = {"Greedy": greedy, "DP": dp_min_coins, "DP_memo": memo_dp}


@time_it
def run_foo(foo, amount):
    return foo(amount)


def comparison(amount):
    time_array = []

    for name, foo in foo_to_compare.items():
        res = run_foo(foo, amount)
        time_array.append(res[1])

        print(f"{name} Result: {res[0], 'Time: ', res[1]}")
        print("*" * 50)

    print(
        "\n",
        "The fastest algorithm is number: ",
        time_array.index(min(time_array)) + 1,
        " with time: ",
        min(time_array),
    )


if __name__ == "__main__":
    amount = int(
        input(
            "Enter the amount you want to get from the collection of coins [2, 3, 5, 6, 11, 13]--> "
        )
    )
    print("*" * 50)
    print()

    comparison(amount)
