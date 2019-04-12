class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def others(self, nums: list, target: int) -> list:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return [nums_dict[nums[i]], i]
            else:
                nums_dict[target - nums[i]] = i


if __name__ == '__main__':
    s = Solution().others([4, 1, 7, 2], 3)
    print(s)
