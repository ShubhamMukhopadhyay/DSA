# Determine Whether Matrix Can Be Obtained By Rotation

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | October 10, 2026 |
| **Tags** | Array, Matrix |
| **Link** | [View Problem](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/) |
| **Runtime** | 3 ms |
| **Memory** | 12.4 MB |

## Problem Description

<p>Given two <code>n x n</code> binary matrices <code>mat</code> and <code>target</code>, return <code>true</code><em> if it is possible to make </em><code>mat</code><em> equal to </em><code>target</code><em> by <strong>rotating</strong> </em><code>mat</code><em> in <strong>90-degree increments</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;">
<pre><strong>Input:</strong> mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise to make mat equal target.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;">
<pre><strong>Input:</strong> mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make mat equal to target by rotating mat.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;">
<pre><strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == mat.length == target.length</code></li>
	<li><code>n == mat[i].length == target[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>mat[i][j]</code> and <code>target[i][j]</code> are either <code>0</code> or <code>1</code>.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Python: 4 Times matrix rotation: Time = O(n^2),  Space = Constant
**Author**: [@meaditya70](https://leetcode.com/meaditya70/)
**Upvotes**: 13 👍
**Link**: [View Original Post](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/1254071/)

---

```
An easy way to Rotate a matrix once by 90 degrees clockwise, 
is to get the **transpose of a matrix and interchange the \'j\'th and \'n-1-j\'th column**, 
for 0<=j<=n-1 where n is the number of columns in matrix.
```
![image](https://assets.leetcode.com/users/images/ba28444c-1388-4092-ba5b-1d5612a06eb6_1622952868.9208376.png)
```
To get the transpose:
			for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
To interchange columns:
			 for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j]
As soon as we get that the rotated matrix is equal to  target, we simply return true,
else we rotate it again(at max 4 times, as we will get the original matrix back after 4th rotation).
```

The full code:
```
def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for times in range(4):
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j] # swap(mat[i][j],mat[j][i])
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j] #swap(mat[i][j], mat[i][n-1-j])
            if(mat == target):
                return True
        return False
```

</details>
