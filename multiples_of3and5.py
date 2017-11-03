def counting():
    i = 1000
    result = 0
    while i > 2:
        i -= 1
        if i % 5 == 0 or i % 3 == 0:
            result += i
    return result


if __name__ == '__main__':
    print(counting())
