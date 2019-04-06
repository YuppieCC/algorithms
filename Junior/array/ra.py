class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if k == 0 or nums_len == 1:
            return None
        if k > nums_len:
            k -= nums_len
        for final_position in range(k):
            start, stop = nums_len - k + final_position, final_position - 1
            for i in range(start, stop, -1):
                if i == final_position:
                    break
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    def rotate_from_others(self, nums: list, k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    s = Solution()
    s.rotate_f([1, 2, 4, 5, 7, 8, 10, 123, 2], 4)
