class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        print(s)


if __name__ == '__main__':
    ip = ["h", "e", "l", "l", "o"]
    Solution().reverseString(ip)
