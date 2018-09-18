"""
整数背包问题

lintcode 92

在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。
"""


# 递归
def backPack(m, A):
    if m <= 0 or len(A) == 0:
        return 0

    if len(A) == 1:
        if m >= A[0]:
            return A[0]
        else:
            return 0

    if m >= A[0]:
        return max(A[0] + backPack(m - A[0], A[1:]), backPack(m, A[1:]))
    else:
        return backPack(m, A[1:])


def backPack2(m, A):
    if m <= 0 or len(A) == 0:
        return 0

    res = [[0] * m for i in range(len(A))]

    pass  # 还不会写


# 别人的动态规划
def backPack3(m, A):
    n = len(A)
    f = [[False] * (m + 1) for _ in range(n + 1)]  # 二维数组

    f[0][0] = True
    for i in range(1, n + 1):
        f[i][0] = True
        for j in range(1, m + 1):
            if j >= A[i - 1]:
                f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
            else:
                f[i][j] = f[i - 1][j]

    for i in range(m, -1, -1):
        if f[n][i]:
            return i
    return 0


if __name__ == '__main__':
    m = 50
    # A = [3, 4, 8, 5]
    A = [16, 16, 3, 5, 16]
    # A = [12, 3, 7, 4, 5, 13, 2, 8, 4, 7, 6, 5, 7]
    print(backPack(m, A))
    print(backPack2(m, A))
    print(backPack3(m, A))
