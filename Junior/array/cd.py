class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        nums[:] = sorted(nums)  # 先排序
        nums_len = len(nums)
        for i in range(nums_len):
            if i + 1 == nums_len:
                break
            if nums[i] == nums[i + 1]:  # 两两之间对比, 相等则返回 True
                return True
        return False


if __name__ == '__main__':
    ip = [1, 2, 3, 1]
    s = Solution().containsDuplicate(ip)
    print(s)
