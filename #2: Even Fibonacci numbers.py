even_fib_arr = []
prev_to_highest = 0
highest_num = 1
def fib(n):
    global highest_num
    global even_fib_arr
    global prev_to_highest

    i = highest_num
    while highest_num < n:
        val = highest_num + prev_to_highest
        if val % 2 == 0:
            even_fib_arr.append(val)
        prev_to_highest = highest_num
        highest_num = val
        i += 1
    #print(even_fib_arr)
def getSum(N):
    result = 0
    for i in even_fib_arr:
        if i > N:
            break
        result += i
    print(result)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        if highest_num < N:
            fib(N)
        getSum(N)