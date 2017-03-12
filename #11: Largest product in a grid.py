"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler011
"""
def maxValue(grid):
    mul_grid = [[1]*20 for _ in range(20)]

    i = 0
    highestValue = 1
    while i < 20:
        j = 0
        while j < 20:
            #RIGHT
            if j == 0:
                mul_grid[i][j] = multiply(grid, i, j, 0, 1)
            elif j < 17 and grid[i][j] > grid[i][j-1]:
                if grid[i][j-1] !=0:
                    temp = mul_grid[i][j-1] // grid[i][j-1]
                    temp = temp*grid[i][j+3]
                else:
                    temp = multiply(grid, i, j, 0, 1)
                if temp > mul_grid[i][j-1]:
                    mul_grid[i][j] = temp
                    if temp > highestValue:
                        highestValue = temp
                    else:
                        mul_grid[i][j] = mul_grid[i][j-1]
            # else:
            #     mul_grid[i][j] = mul_grid[i][j-1]
            #DIAGNOL
            if (i==0 or j==0) and (i < 17 and j< 17):
                temp = multiply(grid, i, j, 1, 1)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp
            elif (i < 17 and j< 17) and grid[i][j] > grid[i-1][j-1]:
                if grid[i-1][j-1] !=0 :
                    temp = mul_grid[i-1][j-1] // grid[i-1][j-1]
                    temp = temp*grid[i+3][j+3]
                else:
                    multiply(grid, i, j, 1, 1)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp
                    if temp > highestValue:
                        highestValue = temp

            # else:
            #     mul_grid[i][j] = mul_grid[i-1][j-1]

            #DOWN
            if i==0 and i < 17:
                temp = multiply(grid, i, j, 1, 0)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp
            elif i < 17 and grid[i][j] > grid[i-1][j]:
                if grid[i-1][j] !=0:
                    temp = mul_grid[i-1][j] // grid[i-1][j]
                    temp = temp*grid[i+3][j]
                else:
                    temp = multiply(grid, i, j, 1, 0)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp
                    if temp > highestValue:
                        highestValue = temp

            # else:
            #     mul_grid[i][j] = mul_grid[i-1][j]


            #
            #
            #
            # #LEFT
            # if j==3:
            #     mul_grid[i][j] = multiply(grid, i, j, 0, -1)
            # elif j > 3 and grid[i][j] > grid[i][j-4]:
            #     if grid[i][]
            #     temp = multiply(grid, i, j, 0, -1)
            #     if temp > mul_grid[i-1][j-1] and temp > mul_grid[i][j]:
            #         mul_grid[i][j] = temp
            #         if temp > highestValue:
            #             highestValue = temp
            #     elif temp > mul_grid[i][j]:
            #         mul_grid[i][j] = temp
            #     else:
            #         mul_grid[i][j] = mul_grid[i-1][j-1]

            # else:
            #     mul_grid[i][j] = mul_grid[i-1][j-1]
            j += 1
        i += 1
            #UP
    return highestValue

def maxValueTwo(grid):
    mul_grid = [[1]*20 for _ in range(20)]

    i = 0
    highestValue = 1
    while i < 20:
        j = 0
        while j < 20:
            #RIGHT
            if j < 17:
                mul_grid[i][j] = multiply(grid, i, j, 0, 1)
            # else:
            #     mul_grid[i][j] = mul_grid[i][j-1]
            #DIAGNOL
            if (i < 17 and j< 17):
                temp = multiply(grid, i, j, 1, 1)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp
            #DOWN
            if i < 17:
                temp = multiply(grid, i, j, 1, 0)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp

            #left diagnol
            if (i < 17 and j > 3):
                temp = multiply(grid, i, j, 1, -1)
                if temp > mul_grid[i][j]:
                    mul_grid[i][j] = temp

            if highestValue < mul_grid[i][j]:
                highestValue = mul_grid[i][j]
            j += 1
        i += 1
    return highestValue

def multiply(grid, i, j, i_inc,j_inc):
    res = 1
    num = 0
    while num < 4:
        res *= grid[i][j]
        i += i_inc
        j += j_inc
        num += 1
    return res
if __name__ == '__main__':
    grid = []
    for grid_i in range(20):
       grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
       grid.append(grid_t)
    print(maxValueTwo(grid))