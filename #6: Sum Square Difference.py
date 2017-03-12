import math
# sum of squares of n numbers - square of sum of numbers
def sum(n):
    return (n * ((3 * math.pow(n, 3)) + (2 * math.pow(n, 2)) - 3 * n - 2)) // 12
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(int(sum(N)))