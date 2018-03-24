"""
Continuous backpack

This package counts the maximum price of items stored in a backpack at a given
price/weight.
simple input:
3 50 - 3 items with a maximum weight of 50
60 20 - first item for $60 for a weight of 20
100 50 - second item for $100 for a weight of 50
120 30 - third item for $120 for a weight of 30
simple output:
180.000 - maximum price of items that fit in backpack

"""


def max_price(backpack, items):
    pack = []
    result = float()
    for item in sorted(items, key=lambda x: x[0]/x[1], reverse=True):
        if item[1] < backpack[1]:
            pack.append(item[0])
            backpack[0] -= 1
            backpack[1] -= item[1]
        else:
            pack.append((item[0]/item[1]) * backpack[1])
            backpack[0] -= 1
            backpack[1] = 0
    for money in pack:
        result += money
    return result


def main():
    amount, weight = map(int, raw_input().split())

    items = [tuple(map(int, raw_input().split())) for _ in range(amount)]

    print("{:.3f}".format(max_price([amount, weight], items)))


if __name__ == "__main__":
    main()