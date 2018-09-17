"""
不同的路径

lintcode 114

m*n的棋盘，从左下走到右上角，每次只能向右或向上移动一个方格边长的距离、共有多少种走法

"""


# 递归
def uniquePaths(m, n):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    return uniquePaths(m-1, n) + uniquePaths(m, n-1)


# 递归转for循环
# 时间复杂度O(m*n), 空间复杂度O(m*n)
def uniquePaths2(m, n):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    res = [[1 for i in range(n)] for j in range(m)]  # 创建二维数组（不可用[[0] * m] * n）

    for i in range(1, m):
        for j in range(1, n):
            res[i][j] = res[i-1][j] + res[i][j-1]

    return res[m-1][n-1]


# 优化
# 时间复杂度O(m*n), 空间复杂度O(n)
def uniquePaths3(m, n):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    res = [1] * n

    for i in range(1, m):
        tmp = [1] * n
        for j in range(1, n):
            tmp[j] = res[j] + tmp[j-1]
        res = tmp

    return res[-1]


# 神奇的解法 使用组合数 来自lintcode题解  why？？？
# 时间复杂度O(n), 空间复杂度O(1)
def uniquePaths4(m, n):
    a = 1
    b = 1
    for i in range(m - 1):
        a = a * (m + n - 2 - i)
        b = b * (i + 1)
    return int(a / b)


if __name__ == "__main__":
    m = 12
    n = 6
    print(uniquePaths(m, n))
    print(uniquePaths2(m, n))
    print(uniquePaths3(m, n))
    print(uniquePaths4(m, n))
