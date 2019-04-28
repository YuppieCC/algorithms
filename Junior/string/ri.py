class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x = str(x)
        while True:
            if x[-1] != '0':
                if x.startswith('-'):
                    res = int('-' + x.replace('-', '')[::-1])
                    if res < -2 ** 31:
                        return 0
                    return res
                else:
                    res = int(x[::-1])
                    if res > (2 ** 31 - 1):
                        return 0
                    return res
            x = x[:-1]


if __name__ == '__main__':
    ip = 1534236469
    op = Solution().reverse(ip)
    print(op)
