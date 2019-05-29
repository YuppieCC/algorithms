# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# not complete
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head.next is None:
            return head
        point = head
        while True:
            temp = point
            print(temp.val)
            for _ in range(n):
                _cur = temp.next
                temp = _cur
            if temp.next is None:
                next_node = point.next
                after_node = point.next.next
                next_node.val = after_node.val
                next_node.next = after_node.next
                break
            point = point.next

        while True:
            if head.next is None:
                print(head.val)

                break
            print(head.val)
            head = head.next


if __name__ == '__main__':
    _1, _2, _3, _4, _5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    _1.next = _2
    _2.next = _3
    _3.next = _4
    _4.next = _5
    _5.next = None
    n = 2
    s = Solution().removeNthFromEnd(_1, 2)
