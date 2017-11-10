import time
import find_prime_factors


def creating_prime_factors_dictionary(number):
    prime_factors_list = find_prime_factors.finding_prime_factors(number)
    prime_factors_dict = dict()
    list_length = len(prime_factors_list)
    i = list_length - 1
    while i > 0:  # sorting the prime factors list
        while prime_factors_list[i - 1] > prime_factors_list[i]:
            temp = prime_factors_list[i - 1]
            prime_factors_list[i - 1] = prime_factors_list[i]
            prime_factors_list[i] = temp
            if i < list_length - 1:
                i += 1
        i -= 1
    i = 0
    while i < list_length:  # creating the dictionary
        digit = prime_factors_list[i]
        number_of_digits = 1
        while i < list_length - 1 and digit == prime_factors_list[i + 1]:
            number_of_digits += 1
            i += 1
        prime_factors_dict[digit] = number_of_digits  # adding new key+value to the dictionary
        i += 1
    return prime_factors_dict


if __name__ == '__main__':
    start_time = time.time()
    print(creating_prime_factors_dictionary(121))
    print("--- %s seconds ---" % (time.time() - start_time))
