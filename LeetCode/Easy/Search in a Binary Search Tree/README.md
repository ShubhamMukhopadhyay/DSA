# Search in a Binary Search Tree

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | August 19, 2026 |
| **Tags** | Tree, Binary Search Tree, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/search-in-a-binary-search-tree/) |
| **Runtime** | 0 ms |
| **Memory** | 12.4 MB |

## Problem Description

<p>You are given the <code>root</code> of a binary search tree (BST) and an integer <code>val</code>.</p>

<p>Find the node in the BST that the node's value equals <code>val</code> and return the subtree rooted with that node. If such a node does not exist, return <code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="width: 422px; height: 302px;">
<pre><strong>Input:</strong> root = [4,2,7,1,3], val = 2
<strong>Output:</strong> [2,1,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="width: 422px; height: 302px;">
<pre><strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>7</sup></code></li>
	<li><code>root</code> is a binary search tree.</li>
	<li><code>1 &lt;= val &lt;= 10<sup>7</sup></code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Recursive and Iterative | Faster than 96% | Easy to understand | Python
**Author**: [@Mrmagician](https://leetcode.com/Mrmagician/)
**Upvotes**: 48 👍
**Link**: [View Original Post](https://leetcode.com/problems/search-in-a-binary-search-tree/solutions/544466/)

---

### Recursive approach
```
def recursive(self, root, val):
        def rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return rec(root.right)
                return rec(root.left)
        
        return rec(root)
```

### Iterative approach
```
def iterative(self, root, val):
        temp = root
        while temp:
            if temp.val == val: return temp
            elif temp.val < val: temp = temp.right
            else: temp = temp.left
        return None
```

**I hope that you\'ve found them useful.**
*In that case, please do upvote. It motivates me to write more such posts*

</details>
