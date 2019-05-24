class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        # 超出时间限制，不是最优
        if not strs:
            return ""
        sl = len(strs)
        if sl == 1:
            return strs[0]

        # 获取单词的最小长度
        _str_len = []
        for st in strs:
            if not st:
                return ""
            _str_len.append(len(st))
        min_len = min(_str_len)

        res = ""
        char_index = 0

        while char_index < min_len:
            prefix = strs[0][char_index]
            for i in range(1, sl):
                if prefix != strs[i][char_index]:
                    return res
                # print(sl)
                if i + 1 == sl:  # 最后一个
                    res += prefix
                    char_index += 1
                    # return res
        return res

def test():
    ip = ["flower", "flow", "flight"]
    ip2 = ["dog", "racecar", "car"]
    ip3 = ["ca", "c"]
    s = Solution()
    assert s.longestCommonPrefix(ip) == "fl"
    assert s.longestCommonPrefix(ip2) == ""
    assert s.longestCommonPrefix(ip3) == "c"


if __name__ == '__main__':
    test()
