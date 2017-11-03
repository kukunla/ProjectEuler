def counting():
    i = 1000
    result = 0
    while i > 2:
        i -= 1
        k = i % 5
        m = i % 3
        if k == 0 or m == 0:
            result += i
    return result


if __name__ == '__main__':
    print(counting())
