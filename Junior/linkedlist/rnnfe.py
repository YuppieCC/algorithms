# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head.next is None:
            # 只有一个值
            return []
        point = head
        while True:
            temp = point
            for _ in range(n):
                # 当前的 temp 在 n 个之后是否是 None
                _cur = temp.next
                temp = _cur
            if temp is None:
                # 去掉第一个
                point.val = point.next.val
                point.next = point.next.next
                return head
            if temp.next is None:
                next_node = point.next
                after_node = point.next.next
                if after_node is None: # n 为 1 ，去掉最后一个
                    point.next = None
                    return head
                next_node.val = after_node.val
                next_node.next = after_node.next
                return head
            point = point.next
