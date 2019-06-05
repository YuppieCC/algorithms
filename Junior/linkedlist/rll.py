# Definition
# for singly - linked list.
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            next = head.next  # 缓存当前节点的向后指针，待下次迭代用
            head.next = pre  # 这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
            pre = head  # 作为下次迭代时的（当前节点的）向前指针
            head = next  # 作为下次迭代时的（当前）节点
        return pre


if __name__ == '__main__':
    _1, _2, _3 = ListNode(1), ListNode(2), ListNode(3)
    _1.next = _2
    _2.next = _3
    _3.next = None
    s = Solution().reverseList(_1)
    print("ok")
