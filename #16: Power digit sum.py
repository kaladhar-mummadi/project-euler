sums = [0] * 10001
sums[0] = 2
def getIntArray(n):
    a = [0] * 5000
    a[0] = 1
    carry = 0
    i = 1
    m = 1
    while i <= n:
        j = 0
        temp_sum = 0
        while j < m:
            temp = a[j] * 2 + carry
            a[j] = temp % 10
            carry = temp // 10
            temp_sum += a[j]

            j += 1
        while carry !=0 :
            temp_sum += carry
            a[m] = carry % 10
            carry //= 10
            m += 1

        sums[i] = temp_sum
        i += 1

# def calSum(n):
#     i = 1
#     power = math.pow(2,n)
#     power = str(int(power))
#     res = 0
#
#     for j in power:
#         res += int(j)
#     return res

if __name__ == '__main__':
    T = int(input())
    getIntArray(10000)
    for _ in range(T):
        N = int(input())
        print(sums[N])
