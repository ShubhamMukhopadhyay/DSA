# Balanced Binary Tree

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | August 19, 2026 |
| **Tags** | Tree, Depth-First Search, Binary Tree |
| **Link** | [View Problem](https://leetcode.com/problems/balanced-binary-tree/) |
| **Runtime** | 3 ms |
| **Memory** | 17.1 MB |

## Problem Description

<p>Given a binary tree, determine if it is <span data-keyword="height-balanced" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_6o_" data-state="closed" class=""><strong>height-balanced</strong></button></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;">
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;">
<pre><strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Very Easy || 100% || Fully Explained (C++, Java, Python, JavaScript, Python3)
**Author**: [@PratikSen07](https://leetcode.com/PratikSen07/)
**Upvotes**: 398 👍
**Link**: [View Original Post](https://leetcode.com/problems/balanced-binary-tree/solutions/2428871/)

---

# **Java Solution:**
Runtime: 0 ms, faster than 100.00% of Java online submissions for Balanced Binary Tree.
Memory Usage: 41.9 MB, less than 94.34% of Java online submissions for Balanced Binary Tree.
```
class Solution {
    public boolean isBalanced(TreeNode root) {
        // If the tree is empty, we can say it\u2019s balanced...
        if (root == null)  return true;
        // Height Function will return -1, when it\u2019s an unbalanced tree...
		if (Height(root) == -1)  return false;
		return true;
	}
    // Create a function to return the \u201Cheight\u201D of a current subtree using recursion...
	public int Height(TreeNode root) {
        // Base case...
		if (root == null)  return 0;
        // Height of left subtree...
		int leftHeight = Height(root.left);
        // Height of height subtree...
		int rightHight = Height(root.right);
        // In case of left subtree or right subtree unbalanced, return -1...
		if (leftHeight == -1 || rightHight == -1)  return -1;
        // If their heights differ by more than \u20181\u2019, return -1...
        if (Math.abs(leftHeight - rightHight) > 1)  return -1;
        // Otherwise, return the height of this subtree as max(leftHeight, rightHight) + 1...
		return Math.max(leftHeight, rightHight) + 1;
    }
}
```

# **C++ Solution:**
```
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // If the tree is empty, we can say it\u2019s balanced...
        if (root == NULL)  return true;
        // Height Function will return -1, when it\u2019s an unbalanced tree...
		if (Height(root) == -1)  return false;
		return true;
	}
    // Create a function to return the \u201Cheight\u201D of a current subtree using recursion...
	int Height(TreeNode* root) {
        // Base case...
		if (root == NULL)  return 0;
        // Height of left subtree...
		int leftHeight = Height(root->left);
        // Height of height subtree...
		int rightHight = Height(root->right);
        // In case of left subtree or right subtree unbalanced or their heights differ by more than \u20181\u2019, return -1...
		if (leftHeight == -1 || rightHight == -1 || abs(leftHeight - rightHight) > 1)  return -1;
        // Otherwise, return the height of this subtree as max(leftHeight, rightHight) + 1...
		return max(leftHeight, rightHight) + 1;
    }
};
```

# **Python Solution:**
```
class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
```
            
# **JavaScript Solution:**
```
var isBalanced = function(root) {
    // If the tree is empty, we can say it\u2019s balanced...
    if (root == null)  return true;
    // Height Function will return -1, when it\u2019s an unbalanced tree...
	if (Height(root) == -1)  return false;
	return true;
}
// Create a function to return the \u201Cheight\u201D of a current subtree using recursion...
var Height = function(root) {
    // Base case...
	if (root == null)  return 0;
    // Height of left subtree...
	let leftHeight = Height(root.left);
    // Height of height subtree...
	let rightHight = Height(root.right);
    // In case of left subtree or right subtree unbalanced, return -1...
	if (leftHeight == -1 || rightHight == -1)  return -1;
    // If their heights differ by more than \u20181\u2019, return -1...
    if (Math.abs(leftHeight - rightHight) > 1)  return -1;
    // Otherwise, return the height of this subtree as max(leftHeight, rightHight) + 1...
	return Math.max(leftHeight, rightHight) + 1;
};
```

# **Python3 Solution:**
```
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
```
**I am working hard for you guys...
Please upvote if you found any help with this code...**

</details>
