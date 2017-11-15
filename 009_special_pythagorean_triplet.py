import time


def find_abc(abc_sum):
    c = int(abc_sum/2)
    a = int((abc_sum - c)/2)
    b = abc_sum - c - a
    while a == b or a > b:
        a -= 1
        b += 1
    while (a*a + b*b) != c*c:
        if b == c:
            b -= 1
            a += 1
        if (a*a + b*b) > c*c:
            a -= 1
            c += 1
        if (a*a + b*b) < c*c:
            b += 1
            c -= 1
    return a*b*c

if __name__ == '__main__':
    start_time = time.time()
    print(find_abc(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
