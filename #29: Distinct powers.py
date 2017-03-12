import math
def getDistinct(n):
    res = [0]*(n+1)
    bases = [0] *(n + 1)
    i = 2
    while i <= n:
        res[i] += (n-1)

        if bases[i] !=0 :
            power = int(math.log(i, bases[i])) + 1
            base = pow(bases[i], power)
        else:
            power = 2
            base = pow(i, power)
            bases[i] = i
        base_power = power - 1
        while base <= n:
            total_sum = 0
            if res[i] == n-1:
                j = 2
            else:
                j = (n//base_power) +1
            if bases[base] == 0:
                bases[base] = i

            while j*power <= base_power * n:
                total_sum -= 1
                j += 1
            res[base] = total_sum
            power += 1
            base = pow(bases[i], power)
        i += 1
    return sum(res)

def hackerrank():
    n = int(input())
    print(getDistinct(n))

def projectEuler():
    print("")

if __name__ == '__main__':
    hackerrank()
    #projectEuler()