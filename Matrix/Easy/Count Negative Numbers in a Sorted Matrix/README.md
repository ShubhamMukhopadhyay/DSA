# Count Negative Numbers in a Sorted Matrix

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 29, 2026 |
| **Tags** | Array, Binary Search, Matrix |
| **Link** | [View Problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |
| **Runtime** | 0 ms |
| **Memory** | 13.2 MB |

## Problem Description

<p>Given a <code>m x n</code> matrix <code>grid</code> which is sorted in non-increasing order both row-wise and column-wise, return <em>the number of <strong>negative</strong> numbers in</em> <code>grid</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you find an <code>O(n + m)</code> solution?

##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: 4 Python Solutions
**Author**: [@pearl_veronica](https://leetcode.com/pearl_veronica/)
**Upvotes**: 104 👍
**Link**: [View Original Post](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/solutions/514468/)

---

**O(n^2) solution**
The Brute Force approach by iterating through matrix row-wise and column wise: 
```
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)-1, -1,-1):
            for j in range(len(grid[0])-1,-1, -1):
                if grid[i][j]<0:
                    count +=1
        return(count)
```
**O(n^2) solution using sum()**
Same as Brute Force but more "condensed" 1-liner code: 
```
    def countNegatives(self, grid):
        return sum(a<0 for i in grid for a in i)
```

**O(m+n) solution**
Counting the negatives in each row:
```
class Solution(object):
    def countNegatives(self, grid):
        i = len(grid)-1
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            print(i,j)
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)
```

**O(mlogn) solution using binary search**
(referred - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510303/Java-solution-%3A-n(log-n) )
```
class Solution(object):
    def countNegatives(self, grid):
        def bin(row):
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]<0:
                    end = mid
                else:
                    start = mid+1
            return len(row)- start
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)
```

Hope this helps! :)

</details>
