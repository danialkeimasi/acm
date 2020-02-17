def check(number):
    number = str(number)
    a, b, number = number[:1], number[1:2], number[2:]

    while number:
        expected = str(int(a) + int(b))
        if number.find(expected) != 0:
            return False

        a, b, number = b, number[:len(expected)], number[len(expected):]

    return True


if __name__ == "__main__":
    print('correct' if check(input()) else 'incorrect')
