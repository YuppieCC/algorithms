## Delete Node in a Linked List
	
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node. Given linked list -- head = [4,5,1,9], which looks like following:

```
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling y
```
```
Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```


Note:

* The linked list will have at least two elements.
* All of the nodes' values will be unique.
* The given node will not be the tail and it will always be a valid node of the linked list.
* Do not return anything from your function.


## Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.
```
Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

Note:

* Given n will always be valid.
* Follow up: Could you do this in one pass?


