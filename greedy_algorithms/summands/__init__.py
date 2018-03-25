from math import sqrt


def summands(number):
    if number == 0:
        print(0)
        return [0]
    elif number < 3:
        print(1)
        return [number]
    elif number < 30:
        range_number = number
    elif number < 100000:
        range_number = number / 2
    else:
        range_number = sqrt(number) * 2

    counter = 0
    numbers = []
    i = 1
    sum_all = 0
    while i < range_number:
        if sum_all == 0 or number - (sum_all + i + i) > 0 or sum_all + i == number:
            numbers.append(i)
            sum_all += i
            counter += 1
        i += 1

    print(counter)
    return numbers


def main():

    get_summands = summands(int(raw_input()))
    for item in get_summands:
        print item,


if __name__ == "__main__":
    main()
