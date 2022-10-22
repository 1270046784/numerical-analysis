# -*-coding:utf-8-*-
# File:17.py
# create by Yu Chen on 2022/10/21
def calc(n):
    """实现数列求和公式"""

    def _calc():
        """正序求和计算"""
        res = 0
        for i in range(2, n + 1):
            res += 1 / (i * i - 1)
        return res

    def _calc_reverse():
        """倒序求和计算"""
        res = 0
        for i in range(n, 1, -1):
            res += 1 / (i * i - 1)
        return res

    print(f'计算S_{n}:')
    print(f'正序计算结果:{_calc()}')
    print(f'倒序计算结果:{_calc_reverse()}\n')


if __name__ == '__main__':
    calc(100)
    calc(10000)
    calc(1000000)
