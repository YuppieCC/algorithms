class Solution:
    def singleNumber(self, nums: list) -> int:
        nums.sort()  # 先排序
        nums_len = len(nums)
        for i in range(0, nums_len, 2):  # step 为 2 , 两两之间比较，不相等则返回第一个
            if i == (nums_len - 1):
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]


if __name__ == '__main__':
    ip = [2, 2, 1]
    op = Solution().singleNumber(ip)
    print(op)
