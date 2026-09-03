# Kth Smallest Element in a BST

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | September 3, 2026 |
| **Tags** | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |
| **Runtime** | 4 ms |
| **Memory** | 20.2 MB |

## Problem Description

<p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;">
<pre><strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Python Easy Iterative and Recursive Solution
**Author**: [@girikuncoro](https://leetcode.com/girikuncoro/)
**Upvotes**: 222 👍
**Link**: [View Original Post](https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/63829/)

---

Recursive:

    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


Iterative:

    def kthSmallest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

</details>
