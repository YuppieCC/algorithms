class Solution:
    def moveZeroes(self, nums: list):
        """
        Do not return anything, modify nums in-place instead.
        [0, 0, 1, 2] -> nums[0] = nums[2]
        [1, 0, 1, 2] -> nums[1] = nums[3]
        [1, 2, 1, 2] -> nums[2] = 0
        [1, 2, 0, 2] -> nums[3] = 0
        [1, 2, 0, 0]
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                i += 1
            else:
                i += 1
        while j < len(nums):
            nums[j] = 0
            j += 1


if __name__ == '__main__':
    ip = [0, 0, 1, 2]
    op = Solution().moveZeroes(ip)
    print(op)
