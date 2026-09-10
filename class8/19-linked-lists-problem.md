# 19. Remove Nth Node From End of List

## Problem 

Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
  Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    
  Example 2:
    Input: head = [1], n = 1
    Output: []
    
  Example 3:
    Input: head = [1,2], n = 1
    Output: [1]


## Solution

def removeNthFromEnd(self, head, n):
    dummy = ListNode(0, head)
    Left = dummy
    Right = head

    while n > 0:
        Right = Right.next
        n -= 1
        
    while Right:
        Right = Right.next
        Left = Left.next

    Left.next = Left.next.next
        
    return dummy.next

  time complexity: O(n)
  space complexity: O(1)

  ## Explanation

  def removeNthFromEnd(self, head, n): // function with head and nth value from the list tail
  
    dummy = ListNode(0, head)   // create dummy node that will come before the head node (0, head)
    Left = dummy               // create a left pointer starting at the dummy node
    Right = head              // create a right pointer starting at the head (first node)

    // Setting up the right pointer so it is located at the node right before the nth node
    
    while n > 0:              // first while loop - while the nth node is greater than zero do the following
        Right = Right.next   // right pointer to the next node
        n -= 1              // right pointer and stops right before the nth value
        
    while Right:              // second while loop - while there is another node for the right pointer to move to
        Right = Right.next   // move the right pointer to the next node
        Left = Left.next    // move the left pointer to the next node

    Left.next = Left.next.next   // remove the nth node by connecting (pointing) the node before it to the node after 
                                // Ex. node_3 ---> node_5 (skips/removes node_4)
        
    return dummy.next // return to the dummy which always keeps a reference to the start (head). Dummy (0), .next (1)

  ### Explanation Summary

  - Create function with head and the nth value.
  - Use two pointers that span the number of nodes designated by n. Ex. n=2
    - so that when the right pointer reaches the end of the list (None), the left pointer stops at the       node before the nth node we want to remove.
    - The left pointer needs to stop before the nth node so that we can remove it by connecting the          node before the nth node to the node after it (using Left.next = Left.next.next).
  - To ensure the left pointer stops before the nth node and not at it, we must create a dummy node        located before the head (0).
    
  - Create a dummy node: dummy = ListNode(0, head)
  - Create left pointer starting at dummy(0): Left = dummy
  - Create right pointer starting at head(1): Right = head

First While Loop

- Positions the pointers moving the right pointer (right.next) by n nodes and stops 1 node before the    nth node (n -= 1). We want the right pointer positioned at the node right before the nth node.
        while n > 0:
            Right = Right.next
            n -= 1

  Second While Loop

- While the right pointer has a node to point at (while Right:) this loop moves left and right           pointers through the list until the right pointer reaches the end of the list (None).
- When the right pointer reaches the end of the list, the left pointer should be located at the node     immediately preceding the nth node.
        while Right:
            Right = Right.next
            Left = Left.next
  Remove the Nth Node
  
- Once in this position, we remove the nth node by connecting the prior nth node to the posterior nth    node: Left.next = Left.next.next.

Return the Head

- return the head by using dummy.next because the dummy always keeps a reference to the start (head).

Example:
head = [0,1,2,3,4,5,None] , n=2
        L     R
