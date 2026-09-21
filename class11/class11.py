'''
Binary Tree DFS

DFS: Depth-First Search
- goes as deep as possible in one path before coming back

two ways to do dfs on trees:

bottom-up dfs:

def dfs(node):
    if not node:
        return base_case

    left = dfs(node.left)
    right = dfs(node.right)

    # use left/right to calculate something

    return something

top-down dfs:

def dfs(node, state):
    if not node:
        return base_case

    new_state = ...

    dfs(node.left, new_state)
    dfs(node.right, new_state)


root = [1,2,3,4,5,null,null]

        1
       / \
      2   3
     / \
    4   5

Preorder: Node -> Left -> Right

def dfs(node):
    if not node:
        return

    print(node.val)
    dfs(node.left)
    dfs(node.r ight)

Result = 1 2 4 5 3

Inorder: Left -> Node -> Right

def dfs(node):
    if not node:
        return

    dfs(node.left)
    print(node.val)
    dfs(node.right)

Result = 4 2 5 1 3

Postorder: Left -> Right -> Node

def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
    print(node.val)

Result = 4 5 2 3 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1

        return dfs(root)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def dfs(node, curr_sum):
            if not node:
                return False

            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            # left = dfs(node.left, curr_sum)

            # if left:
            #     return True

            # right = dfs(node.right, curr_sum)

            # if right:
            #     return True

            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
  
        return dfs(root, 0)

'''