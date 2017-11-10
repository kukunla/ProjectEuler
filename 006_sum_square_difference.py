import time


def find_sum_square_difference(number):
    sum_of_numbers = 0
    sum_of_squares = 0
    while number > 0:
        sum_of_numbers += number
        sum_of_squares += (number * number)
        number -= 1
    return (sum_of_numbers * sum_of_numbers) - sum_of_squares

if __name__ == '__main__':
    start_time = time.time()
    print(find_sum_square_difference(100))
    print("--- %s seconds ---" % (time.time() - start_time))