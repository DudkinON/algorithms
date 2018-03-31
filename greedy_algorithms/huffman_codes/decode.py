def huffman_decode(pairs, code):
    # create variables
    result = ''
    temp = ''

    # decode encoded string
    for char in code:
        temp += char

        for key in pairs:
            if pairs[key] == temp:
                result += key
                temp = ''

    return result


def main():

    pairs = {}

    # read amount of pairs and length of encoded string
    amount, length = raw_input().split()

    # convert to integer
    amount = int(amount)
    length = int(length)

    # read pairs for decode and add to dictionary 'pairs'
    while amount > 0:
        key, value = raw_input().split(": ")
        pairs[key] = value
        amount -= 1

    # read encoded string
    code = raw_input()

    # check length of encoded string
    assert len(code) == length

    # print result
    print(huffman_decode(pairs, code))


if __name__ == '__main__':
    main()
