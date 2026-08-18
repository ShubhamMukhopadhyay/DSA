# Symmetric Tree

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | August 18, 2026 |
| **Tags** | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/symmetric-tree/) |
| **Runtime** | 0 ms |
| **Memory** | 12.5 MB |

## Problem Description

<p>Given the <code>root</code> of a binary tree, <em>check whether it is a mirror of itself</em> (i.e., symmetric around its center).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;">
<pre><strong>Input:</strong> root = [1,2,2,3,4,4,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;">
<pre><strong>Input:</strong> root = [1,2,2,null,3,null,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it both recursively and iteratively?

##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: 🔥Easy Solutions in Java 📝, Python 🐍, and C++ 🖥️🧐Look at once 💻
**Author**: [@Vikas-Pathak-123](https://leetcode.com/Vikas-Pathak-123/)
**Upvotes**: 771 👍
**Link**: [View Original Post](https://leetcode.com/problems/symmetric-tree/solutions/3290112/)

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
 To check if a binary tree is symmetric, we need to compare its left subtree and right subtree. To do this, we can traverse the tree recursively and compare the left and right subtrees at each level. If they are symmetric, we continue the traversal. Otherwise, we can immediately return false.


# Approach
<!-- Describe your approach to solving the problem. -->
We can define a recursive helper function that takes two nodes as input, one from the left subtree and one from the right subtree. The helper function returns true if both nodes are null, or if their values are equal and their subtrees are symmetric.


# Complexity
- Time complexity:The time complexity of the algorithm is $$O(n)$$, where n is the number of nodes in the binary tree. We need to visit each node once to check if the tree is symmetric.
- Space complexity:
The space complexity of the algorithm is $$O(h)$$, where h is the height of the binary tree. In the worst case, the tree can be completely unbalanced, and the recursion stack can go as deep as the height of the tree.


![image.png](https://assets.leetcode.com/users/images/b427e686-2e5d-469a-8e7a-db5140022a6b_1677715904.0948765.png)


# Please Upvote\uD83D\uDC4D\uD83D\uDC4D
```
Thanks for visiting my solution.\uD83D\uDE0A Keep Learning
Please give my solution an upvote! \uD83D\uDC4D
It\'s a simple way to show your appreciation and
keep me motivated. Thank you! \uD83D\uDE0A
```
# Code
``` Java []
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirror(root.left, root.right);
    }
    
    private boolean isMirror(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) {
            return true;
        }
        if (node1 == null || node2 == null) {
            return false;
        }
        return node1.val == node2.val && isMirror(node1.left, node2.right) && isMirror(node1.right, node2.left);
    }
}

```
```Python []
class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

```
```C++ []
class Solution {
public:
    bool isMirror(TreeNode* left, TreeNode* right) {
    if (!left && !right) return true;
    if (!left || !right) return false;
    return (left->val == right->val) && isMirror(left->left, right->right) && isMirror(left->right, right->left);
}

bool isSymmetric(TreeNode* root) {
    if (!root) return true;
    return isMirror(root->left, root->right);
}

};


```
# Please Comment\uD83D\uDC4D\uD83D\uDC4D
```
Thanks for visiting my solution comment below if you like it.\uD83D\uDE0A
```

</details>
