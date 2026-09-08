# Find the Index of the First Occurrence in a String

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | September 8, 2026 |
| **Tags** | Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm |
| **Link** | [View Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| **Runtime** | 0 ms |
| **Memory** | 12.6 MB |

## Problem Description

<p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> haystack = "sadbutsad", needle = "sad"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> haystack = "leetcode", needle = "leeto"
<strong>Output:</strong> -1
<strong>Explanation:</strong> "leeto" did not occur in "leetcode", so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Beats 100% With this easy Solution in Java || Python || C++ || C# 🔥🔥😊
**Author**: [@Hyassin](https://leetcode.com/Hyassin/)
**Upvotes**: 228 👍
**Link**: [View Original Post](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/4749634/)

---

![Screenshot 2024-02-19 101339.png](https://assets.leetcode.com/users/images/0fa6782c-1784-431f-acc1-4afd33759d38_1708318348.7866256.png)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The function is trying to find the index of the first occurrence of the `needle` string within the `haystack` string. If the `needle` is not found in the `haystack`, it returns -1.

# Approach
<!-- Describe your approach to solving the problem. -->

1. Use a loop to iterate through the `haystack` string. The loop starts at index `i = 0` and goes up to `i = haystack.length() - needle.length()`. This is done to ensure that there are enough characters left in the `haystack` for the needle to fit.

2. Within the loop, check substrings of length equal to the length of the `needle` starting from the current index `i` up to `i + needle.length()`. If any of these substrings matches the `needle`, return the current index `i`.

3. If the loop completes without finding a match, return -1.

# Complexity
- Time complexity: O(n * m)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: ***O(1)***
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```java []
class Solution {
    public int strStr(String haystack, String needle) {
        for(int i = 0, j = needle.length(); j<=haystack.length(); i++,j++){
            if(haystack.substring(i,j).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}
```
```python []
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```
```C++ []
class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        for (int i = 0; i <= haystack.length() - needle.length(); ++i) {
            if (haystack.substr(i, needle.length()) == needle) {
                return i;
            }
        }
        return -1;
    }
};
```
```C# []
public class Solution {
    public int StrStr(string haystack, string needle) {
        for (int i = 0; i <= haystack.Length - needle.Length; ++i) {
            if (haystack.Substring(i, needle.Length) == needle) {
                return i;
            }
        }
        return -1;
    }
}
```

![Angry.jpg](https://assets.leetcode.com/users/images/2d755677-0d94-4d6b-93cb-f40d3f0027f7_1708318431.365302.jpeg)


</details>
