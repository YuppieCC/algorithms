class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        nl = len(needle)
        hl = len(haystack)
        for i in range(hl):
            if i + nl > hl:
                return -1
            if haystack[i:i + nl] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack, needle = "helllo", "elo"
    res = Solution().strStr(haystack, needle)
    print(res)
