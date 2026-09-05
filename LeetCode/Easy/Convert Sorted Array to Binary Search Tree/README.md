# Convert Sorted Array to Binary Search Tree

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 5, 2026 |
| **Tags** | Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) |
| **Runtime** | 7 ms |
| **Memory** | 15.1 MB |

## Problem Description

<p>Given an integer array <code>nums</code> where the elements are sorted in <strong>ascending order</strong>, convert <em>it to a </em><span data-keyword="height-balanced" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_t_" data-state="closed" class=""><strong><em>height-balanced</em></strong></button></span> <em>binary search tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;">
<pre><strong>Input:</strong> nums = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;">
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;">
<pre><strong>Input:</strong> nums = [1,3]
<strong>Output:</strong> [3,1]
<strong>Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in a <strong>strictly increasing</strong> order.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: An easy Python solution
**Author**: [@Google](https://leetcode.com/Google/)
**Upvotes**: 298 👍
**Link**: [View Original Post](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/35223/)

---

The idea is to find the root first, then recursively build each left and right subtree

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        # @param num, a list of integers
        # @return a tree node
        # 12:37
        def sortedArrayToBST(self, num):
            if not num:
                return None
    
            mid = len(num) // 2
    
            root = TreeNode(num[mid])
            root.left = self.sortedArrayToBST(num[:mid])
            root.right = self.sortedArrayToBST(num[mid+1:])
    
            return root

</details>
