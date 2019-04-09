class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        res = []
        if len(nums1) < len(nums2):
            short_items = nums1
            long_items = nums2
        else:
            short_items = nums2
            long_items = nums1

        for i in range(len(short_items)):
            if short_items[i] in long_items:
                res.append(short_items[i])
                long_items.remove(short_items[i])
        return res

    def others(self, nums1: list, nums2: list) -> list:
        """
        两只数组已经按升序排好序，所以当 i 指针和 j 指针指向的数值相等时，放入新list；
        如果 i 指针指向的数 < j 指针指向的数，那么 i 指针前进；
        如果 i 指针指向的数 > j 指针指向的数，那么 j 指针前进; 错位遍历。
        :param nums1:
        :param nums2:
        :return:
        """
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = Solution().intersect(nums1, nums2)
    print(res)
