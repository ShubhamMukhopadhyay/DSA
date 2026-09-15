# Find All Numbers Disappeared in an Array

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 15, 2026 |
| **Tags** | Array, Hash Table |
| **Link** | [View Problem](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |
| **Runtime** | 36 ms |
| **Memory** | 26.7 MB |

## Problem Description

<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: C++ Short Solution + Python One-Liner, Explained, No Extra Space
**Author**: [@YehudisK](https://leetcode.com/YehudisK/)
**Upvotes**: 62 👍
**Link**: [View Original Post](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/1583652/)

---

**Solution I:**
We know that all the numbers are in the range [1, n].
So we mark all the indices of the numbers we saw by making the number negative.
Then, we iterate through the array again and each number that is positive - we know we never saw that index and we can add it to `res`.

**Time Complexity:** O(n)
**Space Complexity:** O(1)
```
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) 
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1]);
        
        vector<int> res;
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] > 0) res.push_back(i+1);
        
        return res;
    }
};
```
****
**Solutoin II:**
ONE LINER!
We use simple set subtraction
```
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums)+1)) - set(nums)
```
**Like it? please upvote!**

</details>
