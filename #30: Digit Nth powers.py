def calculatePowers():
    res = []
    power = 3
    while power < 7:
        i = 0
        numbers = []
        while i < 10:
            numbers.append(pow(i, power))
            i += 1
        res.append(numbers)
        power += 1
    return res


def hackerrank():
    powers = calculatePowers()
    N = int(input())
    i = 2
    max_limit = powers[N - 3][9] * N
    total_sum = 0
    while i <= max_limit:
        number = i
        digit_sum = 0
        while number != 0:
            digit_sum += powers[N - 3][number % 10]
            number //= 10
        if digit_sum == i:
            total_sum += digit_sum
        i += 1
    print(total_sum)


def projectEuler():
    print("")


if __name__ == '__main__':
    hackerrank()
    # projectEuler()
