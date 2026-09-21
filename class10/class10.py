'''
Recursion + Trees

1. Recursion
- Function that calls itself
- Needs base case and recursive case

2. Fibonacci
- fib(n) = fib(n - 1) + fib(n - 2)

3. Fibonacci Recursion Tree
- Calls go down
- Answers return back up

4. Tree Basics
- Tree = nodes connected in parent-child structure
- Binary tree = max 2 children

5. Tree Array Representation
- Example: [1, 2, 3, 4, 5] 

6. Parent/Child Array Equation
- Left = 2i + 1
- Right = 2i + 2
- Parent = (i - 1) // 2

7. Root
- Top node of the tree

8. Parent and Child
- Parent = node above
- Child = node below

9. Siblings
- Nodes with same parent

10. Leaf Nodes
- Nodes with no children

14. Balanced Binary Tree
- Left/right subtree heights differ by at most 1

15. TreeNode Class
- val
- left
- right


def maxDepth(root):
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left,right) + 1
'''