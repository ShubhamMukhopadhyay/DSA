# Add Digits

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 6, 2026 |
| **Tags** | Math, Simulation, Number Theory |
| **Link** | [View Problem](https://leetcode.com/problems/add-digits/) |
| **Runtime** | 0 ms |
| **Memory** | 12.3 MB |

## Problem Description

<p>Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without any loop/recursion in <code>O(1)</code> runtime?</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: [Java/C++/Python] solution with Math's explained
**Author**: [@hi-malik](https://leetcode.com/hi-malik/)
**Upvotes**: 252 👍
**Link**: [View Original Post](https://leetcode.com/problems/add-digits/solutions/1754046/)

---

`Math\'s Explained :-`
Any number where it\'s digits add to 9 is always divisible by 9. (18, 27, 36, 45, 54, 63, 72, 81, 90, etc.) Therefore the \'digital root\' for any number divisible by 9 is always 9. You can see this even in larger numbers like 99 because 9 + 9 = 18, and then 1 + 8 = 9 still, so the root always becomes 9 for any numbers divisible by 9.

Additionally, 0 always has a digital root of 0 obviously.

The only other cases you need to worry about to find the digital root are when it isn\'t 0 or 9.

So for any number that isn\'t 0 and isn\'t divisible by 9, the root will always n % 9 for a given number n. (AKA the difference between given number n and the nearest number that is divisible by 9, since numbers divisible by 9 always have a digital root of 9).
For examples: 100 % 9 = 1 (one greater than 99, which is divisible by 9).
101 % 9 = 2
102 % 9 = 3 and so on.

This explanation/algorithm skips the whole "add digits until there is only 1 remaining", so `the description of this problem seems pretty misleading to me since it makes you think the solution will be something unrelated to the optimal one`. I guess the point of Leetcode is to learn all of these tricks though.

**Java**
```
class Solution {
    public int addDigits(int num) {
        if(num == 0) return 0;
        else if(num % 9 == 0) return 9;
        else return num % 9;
    }
}
```
**C++**
```
class Solution {
public:
    int addDigits(int num) {
        if(num == 0) return 0;
        else if(num % 9 == 0) return 9;
        else return num % 9;
    }
};
```
**Python**
```
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)
```
* **Time Complexity :-** BigO(1)

* **Space Complexity :-** BigO(1)

</details>
