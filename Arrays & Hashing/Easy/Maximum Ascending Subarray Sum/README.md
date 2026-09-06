# Maximum Ascending Subarray Sum

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 6, 2026 |
| **Tags** | Array |
| **Link** | [View Problem](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |
| **Runtime** | 0 ms |
| **Memory** | 12.4 MB |

## Problem Description

<p>Given an array of positive integers <code>nums</code>, return the <strong>maximum</strong> possible sum of an <span data-keyword="strictly-increasing-array" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_6v_" data-state="closed" class="">strictly increasing subarray</button></span> in<em> </em><code>nums</code>.</p>

<p>A subarray is defined as a contiguous sequence of numbers in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,20,30,5,10,50]
<strong>Output:</strong> 65
<strong>Explanation: </strong>[5,10,50] is the ascending subarray with the maximum sum of 65.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [10,20,30,40,50]
<strong>Output:</strong> 150
<strong>Explanation: </strong>[10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [12,17,15,13,10,11,12]
<strong>Output:</strong> 33
<strong>Explanation: </strong>[10,11,12] is the ascending subarray with the maximum sum of 33.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: python 3 solution beat 95%
**Author**: [@AchalGupta](https://leetcode.com/AchalGupta/)
**Upvotes**: 7 👍
**Link**: [View Original Post](https://leetcode.com/problems/maximum-ascending-subarray-sum/solutions/1135736/)

---

```
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count=nums[0]
        final=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=nums[i]
            else:
                count=nums[i]
            final=max(final,count)
        return final
```

</details>
