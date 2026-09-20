# Reverse Integer

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | September 20, 2026 |
| **Tags** | Math |
| **Link** | [View Problem](https://leetcode.com/problems/reverse-integer/) |
| **Runtime** | 16 ms |
| **Memory** | 12.5 MB |

## Problem Description

<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Golfing in Python
**Author**: [@StefanPochmann](https://leetcode.com/StefanPochmann/)
**Upvotes**: 165 👍
**Link**: [View Original Post](https://leetcode.com/problems/reverse-integer/solutions/4055/)

---

Get the `s`ign, get the `r`eversed absolute integer, and return their product if `r` didn't "overflow".

    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)

As compressed one-liner, for potential comparison:

    def reverse(self, x):
        s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r

Anybody got something shorter?

</details>
