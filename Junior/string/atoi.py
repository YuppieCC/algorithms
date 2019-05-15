class Solution:
    def myAtoi(self, strs: str) -> int:
        pass
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

    def others(self, str: str) -> int:
        while str and str[0] == ' ':
            str = str[1:]

        if str and str[0] not in '-+0123456789':
            return 0
        if not str:
            return 0
        tmp = []
        for i in str:
            if i in '-+0123456789':
                if i == '-' and tmp:
                    break

                if i == '+' and tmp:
                    break

                tmp.append(i)

            else:
                if not tmp:
                    continue
                else:
                    print('tmp>0 else break')
                    break
        if len(tmp) == 1 and (tmp[0] in '-+'):
            result = 0
        else:
            result = int(''.join(tmp)) if tmp else 0
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        if result < -2 ** 31:
            result = -2 ** 31
        return result


if __name__ == '__main__':
    ip = '3.14159'
    res = Solution().myAtoi(ip)
    print(res)
