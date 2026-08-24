# Delete Node in a BST

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | August 24, 2026 |
| **Tags** | Tree, Binary Search Tree, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/delete-node-in-a-bst/) |
| **Runtime** | 0 ms |
| **Memory** | 20.3 MB |

## Problem Description

<p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return <em>the <strong>root node reference</strong> (possibly updated) of the BST</em>.</p>

<p>Basically, the deletion can be divided into two stages:</p>

<ol>
	<li>Search for a node to remove.</li>
	<li>If the node is found, delete the node.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg" style="width: 800px; height: 214px;">
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 3
<strong>Output:</strong> [5,4,6,2,null,null,7]
<strong>Explanation:</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg" style="width: 350px; height: 255px;">
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>Output:</strong> [5,3,6,2,4,null,7]
<strong>Explanation:</strong> The tree does not contain a node with value = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> root = [], key = 0
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>Each node has a <strong>unique</strong> value.</li>
	<li><code>root</code> is a valid binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= key &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it with time complexity <code>O(height of tree)</code>?</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Python 3 -> 97.55% faster. Explanation added
**Author**: [@mybuddy29](https://leetcode.com/mybuddy29/)
**Upvotes**: 61 👍
**Link**: [View Original Post](https://leetcode.com/problems/delete-node-in-a-bst/solutions/887303/)

---

**Suggestions to make it better are always welcomed.**

Key Learnings for me:
1. First find the node that we need to delete.
2. After it\'s found, think about ways to keep the tree BST after deleting the node. 
	1. If there\'s no left or right subtree, we found the leaf. Delete this node without any further traversing.
	2. If it\'s not a leaf node, what node we can use from the subtree that can replace the delete node and still maintain the BST property? We can either replace the delete node with the minimum from the right subtree (if right exists) or we can replace the delete node with the maximum from the left subtree (if left exists).

```
def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
	if not root:
		return None

	if key > root.val:
		root.right = self.deleteNode(root.right, key)
	elif key < root.val:
		root.left = self.deleteNode(root.left, key)
	else:
		if not root.left and not root.right:
			root = None
		elif root.right:
			root.val = self.successor(root)
			root.right = self.deleteNode(root.right, root.val)
		else:
			root.val = self.predecessor(root)
			root.left = self.deleteNode(root.left, root.val)
	return root

def successor(self, root: TreeNode) -> TreeNode:
	root = root.right
	while root.left:
		root = root.left
	return root.val

def predecessor(self, root: TreeNode) -> TreeNode:
	root = root.left
	while root.right:
		root = root.right
	return root.val
```

**I hope that you\'ve found this useful.
In that case, please upvote. It only motivates me to write more such posts\uD83D\uDE03**

</details>
