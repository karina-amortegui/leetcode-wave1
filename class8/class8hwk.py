'''
Linked List

1. What is a Linked List?

With a normal Python list:
nums = [10, 20, 30]
you can think of the values as sitting next to each other.

A linked list works differently.
Each object stores: value + where the next node is

Example:
10 → 20 → 30 → None

Each individual item is called a node.

2. Node
Typical LeetCode node:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

Each node contains:
- node.val (the value) and node.next (the next node)

Example:
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

node1 -> node2 -> node3

3. head

You'll constantly see keyword "head"
head is simply: the first node of the linked list.
Example:

head
 ↓
10 → 20 → 30 → None

So: 
- head.val => 10
- head.next.val => 20

4. Traversing a Linked List

With an array:
for num in nums:

With a linked list, you usually do:
current = head 
while current:
    print(current.val)
    current = current.next

Example:
10 → 20 → 30 → None

Execution:
current = 10
current = 20
current = 30
current = None

Then stop.
This pattern is extremely important:

current = head
while current:
    current = current.next

You'll use it constantly.
'''

'''
206) Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

21) You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list2.val >= list1.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        # connecting remaining nodes
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next

19) Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head

    slow = dummy
    fast = dummy

    for i in range(n+1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy.next

23) You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res = lists[0]

        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])

        return res
            
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list2.val >= list1.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        # connecting remaining nodes
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next

'''