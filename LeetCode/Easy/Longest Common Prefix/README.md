# Longest Common Prefix

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | October 4, 2026 |
| **Tags** | Array, String, Trie |
| **Link** | [View Problem](https://leetcode.com/problems/longest-common-prefix/) |
| **Runtime** | 4 ms |
| **Memory** | 12.4 MB |

## Problem Description

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Java✅ || C++ || Python || Beats 100% || Beginner's Friendly
**Author**: [@ayeshakalsoom06](https://leetcode.com/ayeshakalsoom06/)
**Upvotes**: 244 👍
**Link**: [View Original Post](https://leetcode.com/problems/longest-common-prefix/solutions/4182958/)

---

![image.png](https://assets.leetcode.com/users/images/cc7a6c16-5ad3-4bf4-a6e9-9e6f9a09f789_1697647919.2392004.png)

# Intuition
To find the longest common prefix among an array of strings, we can compare the characters of all strings from left to right until we encounter a mismatch. The common prefix will be the characters that are the same for all strings until the first mismatch.


# Approach
- If the input array strs is empty, return an empty string because there is no common prefix.

- Initialize a variable prefix with an initial value equal to the first string in the array strs[0].

- Iterate through the rest of the strings in the array strs starting from the second string (index 1).

- For each string in the array, compare its characters with the characters of the prefix string.

- While comparing, if we find a mismatch between the characters or if the prefix becomes empty, return the current value of prefix as the longest common prefix.

- After iterating through all strings, return the final value of prefix as the longest common prefix.

# Complexity
- Time complexity:
O(n * m), where n is the number of strings in the array, and m is the length of the longest string.

- Space complexity:
O(m), where m is the length of the longest string, as we store the prefix string.

# Java
```
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = strs[0];
        for (String s : strs)
            while (s.indexOf(prefix) != 0)
                prefix = prefix.substring(0, prefix.length() - 1);
        return prefix;
    }
}
```

# Python
```
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```


# C++
```
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];
        for (string s : strs)
            while (s.find(prefix) != 0)
                prefix = prefix.substr(0, prefix.length() - 1);
        return prefix;
    }
};

```

![ejw70Xlg.png](https://assets.leetcode.com/users/images/23402a84-eb77-429a-ab73-bd0a81efd39b_1697648099.9098878.png)


</details>
