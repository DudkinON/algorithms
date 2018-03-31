def huffman_decode(pairs, code):
    result = ''
    temp = ''
    for char in code:
        if len(temp):
            temp += char
        else:
            temp = char

        for key in pairs:
            if pairs[key] == temp:
                result += key
                temp = ''
    return result


def main():
    pairs = {}
    amount, length = raw_input().split()
    amount = int(amount)
    length = int(length)

    while amount > 0:
        key, value = raw_input().split(": ")
        pairs[key] = value
        amount -= 1

    code = raw_input()

    assert len(code) == length

    print(huffman_decode(pairs, code))


if __name__ == '__main__':
    main()
