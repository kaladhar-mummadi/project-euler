"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler018

check out

https://www.hackerrank.com/contests/projecteuler/challenges/euler067 for better solution
"""
def tempCalc(arr, rowIndex, colIndex, res):
    global sum
    arrayLength = len(arr)
    if rowIndex == arrayLength - 1:
        return arr[rowIndex][colIndex]
    leftSum = tempCalc(arr, rowIndex + 1, colIndex, res)
    rightSum = tempCalc(arr, rowIndex + 1, colIndex + 1, res)
    if leftSum > rightSum:
        res = leftSum + arr[rowIndex][colIndex]
    else:
        res = rightSum + arr[rowIndex][colIndex]
    return res

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = []
        for _ in range(N):
            row = [int(temp) for temp in input().split(' ')]
            arr.append(row)
        res = 0
        print(tempCalc(arr, 0, 0, 0))