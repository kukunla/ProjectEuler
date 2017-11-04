import time


def finding_largest_palindrome():
    first_multiplier = 999
    largest_palinrome = 0
    while first_multiplier > 99:
        second_multiplier = 999
        while first_multiplier <= second_multiplier:
            result = first_multiplier * second_multiplier
            if is_palindrome(result) and result > largest_palinrome:
                largest_palinrome = result
                print("%s * %s == %s" % (first_multiplier, second_multiplier, result))
            second_multiplier -= 1
        first_multiplier -= 1
    return largest_palinrome


def is_palindrome(result):
    number = str(result)
    i = 0
    j = len(number) - 1
    while number[i] == number[j] and i <= j:
        i += 1
        j -= 1
    return i >= j


if __name__ == '__main__':
    start_time = time.time()
    print(finding_largest_palindrome())
    print("--- %.3f seconds ---" % (time.time() - start_time))
    # print(is_palindrome('00100'))
