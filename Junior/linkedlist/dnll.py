# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 先找出 node 的下一个节点和下下一个节点
        next_node = node.next
        after_node = node.next.next
        # 把节点的值和下一个值互换，把节点的下一个节点接到下下个节点
        node.val = next_node.val
        node.next = after_node
