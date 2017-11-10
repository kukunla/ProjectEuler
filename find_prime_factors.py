import time


def finding_prime_factors(x):
    number = x
    prime_factors_list = list()
    while number % 2 == 0:  # counting twos in an even number
        number /= 2
        prime_factors_list.append(2)
    n = 3
    while number > 1:  # finding prime factors of an odd number
        while number % n == 0:
            number /= n
            prime_factors_list.append(n)
        n += 2
    return prime_factors_list


if __name__ == '__main__':
    start_time = time.time()
    print(finding_prime_factors(120))
    print("--- %s seconds ---" % (time.time() - start_time))
