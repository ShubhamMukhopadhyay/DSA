# Single Number

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 8, 2026 |
| **Tags** | Array, Bit Manipulation |
| **Link** | [View Problem](https://leetcode.com/problems/single-number/) |
| **Runtime** | 9395 ms |
| **Memory** | 14 MB |

## Problem Description

<p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Python different solutions.
**Author**: [@OldCodingFarmer](https://leetcode.com/OldCodingFarmer/)
**Upvotes**: 482 👍
**Link**: [View Original Post](https://leetcode.com/problems/single-number/solutions/43000/)

---

   
    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key
    
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)
        
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

</details>
