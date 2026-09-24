# Majority Element II

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | September 24, 2026 |
| **Tags** | Array, Hash Table, Sorting, Counting, Boyer–Moore Majority Vote Algorithm |
| **Link** | [View Problem](https://leetcode.com/problems/majority-element-ii/) |
| **Runtime** | 9 ms |
| **Memory** | 15.1 MB |

## Problem Description

<p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>⌊n / 3⌋</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Boyer-Moore Majority Vote algorithm and my elaboration
**Author**: [@orbuluh](https://leetcode.com/orbuluh/)
**Upvotes**: 861 👍
**Link**: [View Original Post](https://leetcode.com/problems/majority-element-ii/solutions/63520/)

---

For those who aren't familiar with Boyer-Moore Majority Vote algorithm, 
I found a great article (http://goo.gl/64Nams) that helps me to understand this fantastic algorithm!!
Please check it out!

The essential concepts is you keep a counter for the majority number **X**. If you find a number **Y** that is not **X**, the current counter should deduce 1. The reason is that if there is 5 **X** and 4 **Y**, there would be one (5-4) more **X** than **Y**. This could be explained as "4 **X** being paired out by 4 **Y**".

And since the requirement is finding the majority for more than ceiling of [n/3], the answer would be less than or equal to two numbers. 
So we can modify the algorithm to maintain two counters for two majorities.

Followings are my sample Python code:

    class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

</details>
