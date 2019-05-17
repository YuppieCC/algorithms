class Solution:
    def countAndSay(self, n: int) -> str:
        """
        :type n: int
        :rtype: str
        """
        basic_count_say = "1"
        for num in range(n - 1):  # 从第二个报数开始计算
            basic_count_say = self.transform(basic_count_say)  # 调用报数变换函数
        return basic_count_say

    def transform(self, basic_count_say):  # 报数变换
        count = 0  # 某个数字连续出现的次数
        temp_cha = basic_count_say[0]  # 当前数字
        new_str = ""  # 新的报数序列
        for cha in basic_count_say:  # 遍历旧的报数序列
            print("cha: ", cha)
            if temp_cha == cha:  # 相同连续数字累加
                count += 1
            else:  # 出现不相同数字就补充新报数序列
                new_str = new_str + str(count) + temp_cha
                print("new_str: ", new_str)
                temp_cha = cha  # 清零，从头累加新的数字
                count = 1
        new_str = new_str + str(count) + temp_cha  # 最后一个数字补充到新报数序列中
        print("new_str: ", new_str)
        return new_str


if __name__ == '__main__':
    ip = 1
    res = Solution().countAndSay(3)
    print(res)
