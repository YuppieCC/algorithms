class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = ''.join(s.split())
        _s = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                _s += char
        _sl = len(_s)
        sl = len(_s) // 2
        if _sl == 1:
            return True
        print(_s, sl)
        for i in range(sl):
            if _s[i].lower() == _s[-(i + 1)].lower():
                if i + 1 == sl:
                    return True
                continue
            return False

    def others(self, s):
        s1 = []
        for i in range(len(s)):
            if s[i].isalnum():  # 选择字母或数字
                s1.append(s[i].lower())
        if s1 == s1[::-1]:  # 翻转后是否与之前的相等
            return True
        else:
            return False


if __name__ == '__main__':
    # ip = "A man, a plan, a canal: Panama"
    # ip = "race a car"
    ip = "a."
    r = Solution().isPalindrome(ip)
    print(r)
