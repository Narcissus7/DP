"""
斐波那契数列 求fib(n)的值
"""


# 递归
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)


# 递归转for循环  以空间换时间
def fibonacci2(n):
    if n < 2:
        return n

    res = [0] * n

    res[0] = 1
    res[1] = 1

    for i in range(n):
        if i > 1:
            res[i] = res[i-1]+res[i-2]

    return res[-1]


# 更低空间复杂度  // 不知道有没有可能更低时间复杂度
def fibonacci3(n):
    if n < 2:
        return n

    tmp = 1
    res = 1

    for i in range(2, n):
        res, tmp = res+tmp, res

    return res


if __name__ == '__main__':
    n = 10
    print(fibonacci(n))
    print(fibonacci2(n))
    print(fibonacci3(n))
    # for i in range(1, n):
    #     print(fibonacci2(i))
