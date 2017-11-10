import time


def finding_smallest_multiple(x):
    multiple_of2biggestfactors = (x) * (x - 1)
    multiple = multiple_of2biggestfactors
    smallest_factor = finding_smallest_factor(x)
    x = x - 2
    a = x
    while True:
        print(multiple)
        while (multiple % x) == 0 and x >= smallest_factor:
            if x == 2:
                return multiple
            x -= 1
        multiple += multiple_of2biggestfactors
        x = a


def finding_smallest_factor(x):
    i = 2
    while (x % i) != 0:
        i += 1
    return i+1

if __name__ == '__main__':
    start_time = time.time()
    print(finding_smallest_multiple(20))
    print("--- %.3f seconds ---" % (time.time() - start_time))
