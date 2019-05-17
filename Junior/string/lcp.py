class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        # 超出时间限制，不是最优
        if not strs:
            return ""

        # 获取单词的最小长度
        _str_len = []
        for st in strs:
            if not st:
                return ""
            _str_len.append(len(st))
        min_len = min(_str_len)

        res = ""
        sl = len(strs)
        char_index = 0

        while char_index < min_len:
            prefix = strs[0][char_index]
            for i in range(1, sl):
                if prefix != strs[i][char_index]:
                    return res
                if i + 1 == sl:
                    res += prefix
                    char_index += 1


def test():
    ip = ["flower", "flow", "flight"]
    ip2 = ["dog", "racecar", "car"]
    s = Solution()
    assert s.longestCommonPrefix(ip) == "fl"
    assert s.longestCommonPrefix(ip2) == ""


if __name__ == '__main__':
    test()
