# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    a = money // 10
    b = money % 10
    c = b // 5
    d = b % 5

    return a + c + d


if __name__ == '__main__':
    # input_money = int(input())
    # print(money_change(input_money))
    amount = 50
    print(money_change(amount))
