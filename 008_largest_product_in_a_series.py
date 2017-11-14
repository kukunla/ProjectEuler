import time

#TODO: @cunla how can I improve this code?

def find_largest_product(number, digits_series_size):
    number_length = len(number)
    i = 0
    series_ending = i + digits_series_size - 1
    largest_product = 0
    while series_ending < number_length:
        series_ending = series_without_zero(number, number_length, digits_series_size, i, series_ending)
        i = series_ending - digits_series_size + 1
        while series_ending < number_length and number[series_ending] != 0:
            current_product = int(number[i])
            while i < series_ending:
                i += 1
                current_product *= int(number[i])
            if current_product > largest_product:
                largest_product = current_product
            series_ending += 1
            i = series_ending - digits_series_size + 1
    return largest_product


def series_without_zero(number, number_length, digits_series_size, i, series_ending):
    if number[series_ending] == 0:
        i = series_ending + digits_series_size
        series_ending = i + digits_series_size - 1
    while i <= series_ending:
        if series_ending >= number_length:
            return series_ending
        if number[i] == 0:
            i += digits_series_size - 1
            series_ending = i + digits_series_size
        i += 1
    return series_ending


if __name__ == '__main__':
    start_time = time.time()
    print(find_largest_product(
        "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450", 13))
    print("--- %s seconds ---" % (time.time() - start_time))
