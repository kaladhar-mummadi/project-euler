"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler067
"""
def tempCalc(arr, rowIndex, colIndex, res, visited):
    arrayLength = len(arr)

    if rowIndex == arrayLength - 1:
        return arr[rowIndex][colIndex]
    if visited[rowIndex][colIndex]:
        return arr[rowIndex][colIndex]
    leftSum = tempCalc(arr, rowIndex + 1, colIndex, res, visited)
    rightSum = tempCalc(arr, rowIndex + 1, colIndex + 1, res, visited)
    if leftSum > rightSum:
        arr[rowIndex][colIndex] = leftSum + arr[rowIndex][colIndex]
    else:
        arr[rowIndex][colIndex] = rightSum + arr[rowIndex][colIndex]
    visited[rowIndex][colIndex] = True
    return arr[rowIndex][colIndex]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = []
        visited = [[False]*N for _ in range(N)]
        for _ in range(N):
            row = [int(temp) for temp in input().split(' ')]
            arr.append(row)
        res = 0
        print(tempCalc(arr, 0, 0, 0, visited))