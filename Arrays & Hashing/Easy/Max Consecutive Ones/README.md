# Max Consecutive Ones

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 20, 2026 |
| **Tags** | Array |
| **Link** | [View Problem](https://leetcode.com/problems/max-consecutive-ones/) |
| **Runtime** | 38 ms |
| **Memory** | 13.5 MB |

## Problem Description

<p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>'s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Clever python solution
**Author**: [@mxmb](https://leetcode.com/mxmb/)
**Upvotes**: 42 👍
**Link**: [View Original Post](https://leetcode.com/problems/max-consecutive-ones/solutions/1067437/)

---

if `consecutive == 1`, `consecutive*n+n == consecutive+1`
if `consecutive == 0`, `consecutive*n+n = 0`.

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = result = 0
        for n in nums:
            consecutive = consecutive*n+n
            result = max(result, consecutive)
        return result
```

</details>
