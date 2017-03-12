import timeit
max = 5000001
max_arr = max * 3
steps = [0] * max_arr
def calcNumbers():
    global steps
    steps[1] = 0
    i = 2
    while i < max:
        local_steps = 0
        num = i
        arr = []
        while steps[i] == 0 and num != 1:
            if num < max_arr and steps[num] != 0:
                break
            if num % 2 == 0 and num < max_arr and steps[num//2] != 0:
                steps[num] = steps[num//2] + 1
                num = num // 2
                local_steps += 1
                break
            elif num % 2 == 0:
                arr.append(num)
                num = num // 2
                local_steps += 1
            else:
                arr.append(num)
                num = num * 3 + 1
                local_steps += 1
        length = len(arr)
        j = 0
        loc = steps[num] + local_steps
        while j < length:
            if arr[j] < max_arr :
                steps[arr[j]] = loc
            loc -= 1
            j += 1

        # if steps[i] == 0:
        #     steps[i] = steps[num] + local_steps
        #     times[i] += 1
        i += 1

def getMax(n):
    max_val = 0
    index = 1
    i = 1
    while i < n:
        if max_val <= steps[i]:
            max_val = steps[i]
            index = i
        i += 1
    print(index)



def hackerank():
    T = int(input())
    for _ in range(T):
        N = int(input())
        getMax(N)

if __name__ == '__main__':
    #start = timeit.default_timer()
    calcNumbers()
    #stop = timeit.default_timer()
    #print(stop - start)
    hackerank()