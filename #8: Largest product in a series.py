def cal(numbers):
    result = 1
    for i in numbers:
        num = int(i)
        result *= num
    return result
def product(str, k):
    numbers = str[0:k]
    consec_product = cal(numbers)
    result = consec_product
    j = k
    length = len(str)
    while j < length:
        if str[j - k] != '0':
            consec_product = consec_product // int(str[j - k])
        else:
            consec_product = cal(str[j - k + 1: j])
        consec_product = consec_product * int(str[j])
        if consec_product > result:
            result = consec_product
        j += 1
    return result
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = input().split(" ")
        N, K = [int(N), int(K)]
        str = input()
        result = product(str, K)
        print(result)
