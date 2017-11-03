def counting_fibonacci():
    first_number = 1
    second_number = 2
    sum_of_even_numbers = 0
    while second_number < 4000000:
        if second_number % 2 == 0:
            sum_of_even_numbers += second_number
        temp = first_number + second_number
        first_number = second_number
        second_number = temp
    return sum_of_even_numbers


if __name__ == '__main__':
    print(counting_fibonacci())
