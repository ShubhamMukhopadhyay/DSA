# Binary Tree Inorder Traversal

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | August 17, 2026 |
| **Tags** | Stack, Tree, Depth-First Search, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| **Runtime** | 0 ms |
| **Memory** | 12.3 MB |

## Problem Description

<p>Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,null,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;"></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,2,6,5,7,1,3,9,8]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/tree_2.png" style="width: 350px; height: 286px;"></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = []</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?

##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: All DFS traversals (preorder, inorder, postorder) in Python in 1 line
**Author**: [@andvary](https://leetcode.com/andvary/)
**Upvotes**: 1090 👍
**Link**: [View Original Post](https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/)

---

![image](https://assets.leetcode.com/users/andvary/image_1556551007.png)

```
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
```

```
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
```

```
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
```


</details>
