import time


def find_10001st_prime(number):
    if number == 1:
        return 2
    prime_numbers_list = [2]
    i = 1
    digit = 1
    while i < number:
        digit += 2
        if is_prime(digit, prime_numbers_list):
            prime_numbers_list.append(digit)
            i += 1
    return digit


def is_prime(digit, prime_numbers_list):
    i = 0
    while (prime_numbers_list[i] * prime_numbers_list[i]) <= digit:
        if (digit % prime_numbers_list[i]) == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    start_time = time.time()
    print(find_10001st_prime(10001))
    print("--- %s seconds ---" % (time.time() - start_time))
