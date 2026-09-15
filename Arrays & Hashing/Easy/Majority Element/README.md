# Majority Element

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 15, 2026 |
| **Tags** | Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm |
| **Link** | [View Problem](https://leetcode.com/problems/majority-element/) |
| **Runtime** | 2 ms |
| **Memory** | 13.5 MB |

## Problem Description

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>⌊n / 2⌋</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that a majority element will exist in the array.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Python different solutions
**Author**: [@OldCodingFarmer](https://leetcode.com/OldCodingFarmer/)
**Upvotes**: 272 👍
**Link**: [View Original Post](https://leetcode.com/problems/majority-element/solutions/51712/)

---

```
class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n
            
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
```

</details>
