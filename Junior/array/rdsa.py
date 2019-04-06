class Solution:
    def removeDuplicates(self, nums) -> int:
        _len = len(nums)
        for first_value in range(_len):
            next_value = first_value + 1
            while next_value < len(nums):
                if nums[first_value] != nums[next_value]:
                    break
                else:
                    del nums[next_value]
        return len(nums)


if __name__ == '__main__':
    ip = [0, 0, 1, 1, 2, 2]
    op = Solution().removeDuplicates(ip)
    print(op)
