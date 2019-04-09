class Solution:
    def plusOne(self, digits: list) -> list:
        digits_len = len(digits)
        i = -1
        while i >= -digits_len:
            if digits[i] == 9:
                digits[i] = 0
                if i == -digits_len:
                    digits[:] = [1] + digits[:]  # [9] -> [1, 0]
                    break
                else:
                    i -= 1
                    continue
            else:
                digits[i] += 1  # 最高位加 1
                break
        return digits


if __name__ == '__main__':
    ip = [9, 9]
    op = Solution().plusOne(ip)
    print(op)  # [1, 0, 0]
