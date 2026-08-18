# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front= -1

    def push(self, x):
        if self.front == -1:
            self.front = 0

        self.q.append(x)

    def pop(self):
        if len(self.q) == 0:
            return -1

        x = self.q[self.front]
        self.front += 1

        if self.front == len(self.q):
            self.front = -1
            self.q = []

        return x

    def getFront(self):
        if len(self.q) == 0:
            return -1

        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
            
        return len(self.q) - self.front

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ans = []

        if root is None:
            return True

        queue = Queue()
        # queue.push(root)
        ans.append([root.val])

        queue.push(root.left)
        queue.push(root.right)

        while queue.size() > 0:
            left = queue.pop()
            right = queue.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False
                
            queue.push(left.left)
            queue.push(right.right)

            queue.push(left.right)
            queue.push(right.left)

        return True
