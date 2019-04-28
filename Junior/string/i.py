class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        sl = len(s)
        for i in range(sl):
            if s[i] not in res:
                res[s[i]] = 1
            else:
                res[s[i]] += 1

        for i in range(sl):
            if res[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    ip = "loveleetcode"
    res = Solution().firstUniqChar(ip)
    print(res)
