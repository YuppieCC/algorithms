class Solution:
    def myAtoi(self, strs: str) -> int:
        # strs = ''.join(strs.split())
        # if not strs:
        #     return 0
        # slen = len(strs)
        # s1 = strs[0]
        # if s1 not in ('+', '-') and not s1.isdigit() or (slen == 1 and not s1.isdigit()):
        #     return 0
        # pn = '-' if s1 == '-' else ''
        # res = ''
        # for i in range(slen):
        #     if i != 0 and not strs[0].isdigit() and not strs[i].isdigit():
        #         break
        #
        #     if res.isdigit() and not strs[i].isdigit():
        #         break
        #     if strs[i].isdigit():
        #         res += strs[i]
        # if res.isdigit():
        #     res = int(pn + res)
        #     if -2 ** 31 < res < 2 ** 31 - 1:
        #         return res
        #     else:
        #         return -2147483648
        # else:
        #     return 0


if __name__ == '__main__':
    ip = '3.14159'
    res = Solution().myAtoi(ip)
    print(res)
