# Validate Binary Search Tree

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | September 3, 2026 |
| **Tags** | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/validate-binary-search-tree/) |
| **Runtime** | 4 ms |
| **Memory** | 17.2 MB |

## Problem Description

<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left <span data-keyword="subtree" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_s_" data-state="closed" class="">subtree</button></span> of a node contains only nodes with keys&nbsp;<strong>strictly less than</strong> the node's key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>strictly greater than</strong> the node's key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;">
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;">
<pre><strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: General Tree Traversal Problems, interview Prep
**Author**: [@pakilamak](https://leetcode.com/pakilamak/)
**Upvotes**: 453 👍
**Link**: [View Original Post](https://leetcode.com/problems/validate-binary-search-tree/solutions/786520/)

---

Please feel free to suggest similar problems in the comment section.

There are three types of Tree traversal: Inorder, Preorder and Postorder

* **Inorder:** left, root, right
* **Preorder:** root, left child, right child **OR**  root, right child, left child			
* **Postorder:** left child, right child, root **OR** right child, left child, root
							
				

**INORDER TRAVERSAL**

**98. Validate Binary Search Tree**

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output =[]
        self.inorder(root, output)
        
        for i in range(1, len(output)):
			if output[i-1]>= output[i]:
				return False
        
        return True
    
    # Time complexity of inorder traversal is O(n)
    # Fun fact: Inorder traversal leads to a sorted array if it is 
    # a Valid Binary Search. Tree.
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
        
```
**94. Binary Tree Inorder Traversal**


```
# Recursive: runtime-16ms

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.inorder(root, output)
        return output
        
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


# Iterative Runtime: 20 ms, faster than 70.13%

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack=[]
        
        while stack or root:
            
            if root:
                stack.append(root)
                root =root.left
                
            else:
                temp =stack.pop()
                output.append(temp.val)
                root= temp.right
           
        return output
```

**PREORDER TRAVERSAL**

**589. N-ary Tree Preorder Traversal**


```
## Recursive Solution: Runtime: 36 ms, faster than 97.16%
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        output =[]
        
        # perform dfs on the root and get the output stack
        self.dfs(root, output)
        
        # return the output of all the nodes.
        return output
    
    def dfs(self, root, output):
        
        # If root is none return 
        if root is None:
            return
        
        # for preorder we first add the root val
        output.append(root.val)
        
        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)
       
	   
	   
# Iterative Solution- Runtime: 40 ms, faster than 91.86% 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = [root]
        output = []
        
        # Till there is element in stack the loop runs.
        while stack:
            
            #pop the last element from the stack and store it into temp.
            temp = stack.pop()
            
            # append. the value of temp to output
            output.append(temp.val)
            
            #add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1])
        
        #return the output
        return output
        
```



**144. Binary Tree Preorder Traversal**


```
# Recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        
        output.append(root.val)
        self.dfs(root.left, output)
        self.dfs(root.right, output)
       
	   
# Iterative Solution- Runtime: 12 ms, faster than 97.82%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output =[]
        stack = [root]
        
        while stack:
            temp=stack.pop()
            if temp:
                output.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        
        return output
```
**257. Binary Tree Paths** : Runtime: 16 ms, faster than 93.92% of Python 
https://leetcode.com/problems/binary-tree-paths/

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append(path + str(root.val))
        
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->" , result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)
        
```


**POSTORDER TRAVERSAL**

**590. N-ary Tree Postorder Traversal**
```
# Recursive : Runtime: 40 ms, faster than 89.79% 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        for child in root.children:
            self.dfs(child, output)
        
        output.append(root.val)
 
 
 # Iterative Solution: Runtime: 48 ms, faster than 62.81%
 
 `"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output =[]
        stack = [root]
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack += root.children
                
        return output[::-1]`
        
```

**145. Binary Tree Postorder Traversal**

```
# Recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        self.dfs(root.left, output)
        self.dfs(root.right, output) 
        output.append(root.val)
		
		
# Iterative solution: Runtime: 12 ms, faster than 98.10%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack =[root]
        
        if not root:
            return None
        
        # iterate only when there is elements inside the stack.
        while stack:
            
            # pop the element from stack and stored it into temp
            temp=stack.pop()
            
            #append the value of temp to output
            output.append(temp.val)
            
            #Now traverse through left node and add the node to stack
            if temp.left:
                stack.append(temp.left)
                
            #else traverse through right node and add to stack
            if temp.right:
                stack.append(temp.right)
         
        # After iterating through the stack,  print the result in reverse order.  
        return output[::-1]
    
    
# Example: Iteration 1 : #stack=[1] - first iteration, temp =1, 
                #output[1]
                #temp.left is Null
                #temp.right is [2]
                # stack =[2]

```

**LEVEL ORDER TRAVERSAL**

**102. Binary Tree Level Order Traversal**
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output =[]
        self.dfs(root, 0, output)
        return output
    
    def dfs(self, root, level, output):
        
        if not root:
            return
        
        if len(output) < level+1:
            output.append([])
            
        output[level].append(root.val)    
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
        
```

**107. Binary Tree Level Order Traversal II**
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        self.dfs(root, 0, output)
        return output[::-1]
    
    def dfs(self, root, level, output):
        if root is None:
             return
            
        if len(output) < level+1:
            output.append([])
            
        output[level].append(root.val)
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
```

**429. N-ary Tree Level Order Traversal**
```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        output=[]
        self.dfs(root, 0, output)
        return output
    
    def dfs(self, root, level ,output):
        if root is None:
            return
        if len(output)< level+1:
            output.append([])
        
        output[level].append(root.val)
        for child in root.children:
            self.dfs(child, level+1, output)
      
```

**103. Binary Tree Zigzag Level Order Traversal**
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output=[]
        self.dfs(root, 0, output)
        
        for i in range(len(output)):
            if i % 2 !=0:
                output[i].reverse()
            else:
                continue
        return output
    
    def dfs(self, root, level, output):
        if root is None:
            return
        
        if len(output) < level+1:
            output.append([])
        
        output[level].append(root.val)
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
        
```


**BINARY TREE CONSTRUCTION**


**105. Construct Binary Tree from Preorder and Inorder Traversal**
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder or not preorder:
            return None
        
        #pattern is preorder=[root, left, right]
        #inorder = [left, root, right],  so find index and value using root.
        
        root = TreeNode(preorder[0])
        
        root_index= 0
        
        #iterate through inorder list and find the list index of the root.
        for i in range(len(inorder)):
            if inorder[i]== root.val:
                root_index = i
            else:
                continue
                
        #slice the inorder list into left and right.     
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        
        #slice the preorder list into left and right.
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_preorder)+1:]
        
        #append by updating preorder and inorder lists
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
```

**106. Construct Binary Tree from Inorder and Postorder Traversal**

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # PATTERN
        # inorder: l, root, right
        # postorder: l,r,root
        # the last element of postorder is root
        
        if not inorder or not postorder:
            return None
        
        root_index=0
        
        # Build the data structure based on root value
        root = TreeNode(postorder.pop())
        
        for i in range(len(inorder)):
            if inorder[i]==root.val:
                root_index=i
            else:
                continue
        
        left_in=inorder[:root_index]
        right_in = inorder[root_index+1:]
        
        root.right = self.buildTree(right_in, postorder)
        root.left = self.buildTree(left_in,  postorder)

        return root
   
```

**889. Construct Binary Tree from Preorder and Postorder Traversal:** 
Runtime: 40 ms, faster than 80.14%

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        
        root = TreeNode(post.pop())
        
        if len(pre) == 1:
            return root
        
        # Find the index of the root value from pre
        for i in range(len(pre)):
            if pre[i]==post[-1]:
                root_index= i
            else:
                continue
        
        root.right = self.constructFromPrePost(pre[root_index:], post) 
        root.left = self.constructFromPrePost(pre[1:root_index],post) 
        
        return root 
   
# Explanation:   root=1, root_index = 0, root.right=(pre(1,2,3,4,5,6,7))  [1, 2,3,4,5,6,7]                           vii
									# root = 3, root_index= 4, root.right=(pre(3,6,7))  [3,4,5,6,7]                               v
											# root=7, root_index=2, root.right= pre(7), now len(pre) == 1, return 7 ---[7]        i
											# root =6, root_index=1, root.left= pre(6), now len(pre)==1, return 6 -----[6,7]      ii 

									# root =2, root_index= 1, root.right= pre(2,4,5)   [2,3,4,5,6,7]                               vi 
											# root = 5, root_index=2, root.right= pre(5)  now len(pre)==1, return 5 ----[5,6,7]   iii
											# root = 4, root_index=1, root.right= pre(4)  now len(pre)==1, return 4-----[4,5,6,7]  iv

```
=========================================================
Hope you\'ve found the solutions useful. Please do UPVOTE, it only motivates me to write more such posts. Thanks!

</details>
