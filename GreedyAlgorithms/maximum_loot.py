# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    prices_per_kg = list(i / j for i, j in zip(prices, weights))

    total_knapsack_value = 0
    if capacity == 0:
        return total_knapsack_value

    while capacity > 0 and len(weights) > 0:
        index_max_val = prices_per_kg.index(max(prices_per_kg))
        weight = weights[index_max_val]

        if capacity <= weight:
            total_knapsack_value += capacity * prices_per_kg[index_max_val]
            return total_knapsack_value

        elif capacity > weight:
            total_knapsack_value += prices[index_max_val]
            prices_per_kg.pop(index_max_val)
            weights.pop(index_max_val)
            prices.pop(index_max_val)
            capacity -= weight

    return total_knapsack_value

    # values = list(p / w for p, w in zip(prices, weights))
    #
    # total_value = 0
    #
    # c = int(capacity)
    #
    # if c == 0:
    #     return total_value
    #
    # while c > 0:
    #     b = values.index(max(values))
    #     if c == weights[b]:
    #         return prices[b]
    #
    #     elif c < weights[b]:
    #         possible = (weights[b]) / capacity
    #         total_value += (prices[b]) / possible
    #         return total_value
    #
    #     elif c > weights[b]:
    #         total_value += prices[b]
    #         c -= weights[b]
    #         del values[b]
    #
    #     return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

    # capacity = 60
    # prices = [60, 100, 120]
    # weights = [20, 50, 30]
    # print(maximum_loot_value(capacity, weights, prices))
