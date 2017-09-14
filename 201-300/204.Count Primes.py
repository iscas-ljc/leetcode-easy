class Solution(object):
    def countPrimes(self, n):
        if n<3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
#从上面的厄拉多塞筛法可以看出，
#我们只需遍历[2,这里写图片描述],因为超过这里写图片描述部分如果不是素数，
#则作为因子在前面的数已经被删除了。同时这里利用了python里list的特性[::i]取i的倍数。