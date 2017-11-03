import math
import time

def finding_prime_factor(x):
    largest_prime_factor = 0
    if x % 2 == 0:
        x = x / 2
    number = 3
    while number <= x:
        number += 2
        if finding_prime_number(number) and x % number == 0:
            largest_prime_factor = number
            x = x / number
    return largest_prime_factor


def finding_prime_number(number):
    if number % 2 == 0:
        return False
    i = 3
    while i < int(math.sqrt(number)):
        if number % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    start_time = time.time()
    print(finding_prime_factor(600851475143))
    print("--- %s seconds ---" % (time.time() - start_time))