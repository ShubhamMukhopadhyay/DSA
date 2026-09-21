# Wiggle Sort II

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python |
| **Solved On** | September 21, 2026 |
| **Tags** | Array, Divide and Conquer, Greedy, Sorting, Quickselect |
| **Link** | [View Problem](https://leetcode.com/problems/wiggle-sort-ii/) |
| **Runtime** | 9 ms |
| **Memory** | 14.3 MB |

## Problem Description

<p>Given an integer array <code>nums</code>, reorder it such that <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>.</p>

<p>You may assume the input array always has a valid answer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,1,1,6,4]
<strong>Output:</strong> [1,6,1,5,1,4]
<strong>Explanation:</strong> [1,4,1,5,1,6] is also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,2,2,3,1]
<strong>Output:</strong> [2,3,1,3,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
	<li>It is guaranteed that there will be an answer for the given input <code>nums</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow Up:</strong> Can you do it in <code>O(n)</code> time and/or <strong>in-place</strong> with <code>O(1)</code> extra space?

##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: 3 lines Python, with Explanation / Proof
**Author**: [@StefanPochmann](https://leetcode.com/StefanPochmann/)
**Upvotes**: 398 👍
**Link**: [View Original Post](https://leetcode.com/problems/wiggle-sort-ii/solutions/77678/)

---

Solution
---

Roughly speaking I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes.

    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

Alternative, maybe nicer, maybe not:

    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

---

**Explanation / Proof**
---

I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:

    Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 

    Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
    Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
    --------------------------      --------------------------
    Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5

I want:

- Odd-index numbers are larger than their neighbors.

Since I put the larger numbers on the odd indexes, clearly I already have:

- Odd-index numbers are larger than **or equal to** their neighbors.

Could they be "equal to"? That would require some number M to appear both in the smaller and the larger half. It would be the largest in the smaller half and the smallest in the larger half. Examples again, where S means some number smaller than M and L means some number larger than M.

    Small half:  M . S . S . S      Small half:  M . S . S . S .
    Large half:  . L . L . M .      Large half:  . L . L . L . M
    --------------------------      --------------------------
    Together:    M L S L S M S      Together:    M L S L S L S M

You can see the two M are quite far apart. Of course M could appear more than just twice, for example:

    Small half:  M . M . S . S      Small half:  M . S . S . S .
    Large half:  . L . L . M .      Large half:  . L . M . M . M
    --------------------------      --------------------------
    Together:    M L M L S M S      Together:    M L S M S M S M

You can see that with seven numbers, three M are no problem. And with eight numbers, four M are no problem. Should be easy to see that in general, with n numbers, floor(n/2) times M is no problem. Now, if there were more M than that, then my method would fail. But... it would also be impossible:

- If n is even, then having more than n/2 times the same number clearly is unsolvable, because you'd have to put two of them next to each other, no matter how you arrange them.
- If n is odd, then the only way to successfully arrange a number appearing more than floor(n/2) times is if it appears exactly floor(n/2)+1 times and you put them on all the even indexes. And to have the wiggle-property, all the other numbers would have to be larger. But then we wouldn't have an M in both the smaller and the larger half.

So if the input has a valid answer at all, then my code will find one.

</details>
