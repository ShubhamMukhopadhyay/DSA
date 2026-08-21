# Missing Number

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python |
| **Solved On** | August 21, 2026 |
| **Tags** | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
| **Link** | [View Problem](https://leetcode.com/problems/missing-number/) |
| **Runtime** | 0 ms |
| **Memory** | 13.4 MB |

## Problem Description

<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><code>n = 3</code> since there are 3 numbers, so all numbers are in the range <code>[0,3]</code>. 2 is the missing number in the range since it does not appear in <code>nums</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><code>n = 2</code> since there are 2 numbers, so all numbers are in the range <code>[0,2]</code>. 2 is the missing number in the range since it does not appear in <code>nums</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,6,4,2,3,5,7,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p><code>n = 9</code> since there are 9 numbers, so all numbers are in the range <code>[0,9]</code>. 8 is the missing number in the range since it does not appear in <code>nums</code>.</p>
</div>

<div class="simple-translate-system-theme" id="simple-translate">
<div>
<div class="simple-translate-button isShow" style="background-image: url(&quot;moz-extension://8a9ffb6b-7e69-4e93-aae1-436a1448eff6/icons/512.png&quot;); height: 22px; width: 22px; top: 318px; left: 36px;">&nbsp;</div>

<div class="simple-translate-panel" style="width: 300px; height: 200px; top: 0px; left: 0px; font-size: 13px;">
<div class="simple-translate-result-wrapper" style="overflow: hidden;">
<div class="simple-translate-move" draggable="true">&nbsp;</div>

<div class="simple-translate-result-contents">
<p class="simple-translate-result" dir="auto">&nbsp;</p>

<p class="simple-translate-candidate" dir="auto">&nbsp;</p>
</div>
</div>
</div>
</div>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: ✅☑Beats 98% Users || 4 Approaches || [C++/Java/Python/JavaScript] || EXPLAINED🔥
**Author**: [@MarkSPhilip31](https://leetcode.com/MarkSPhilip31/)
**Upvotes**: 543 👍
**Link**: [View Original Post](https://leetcode.com/problems/missing-number/solutions/4754401/)

---

# DO GIVE IT A LIKE IF THAT WAS HELPFUL\uD83E\uDEE1\uD83D\uDC47



---
![Screenshot 2024-02-20 060808.png](https://assets.leetcode.com/users/images/1dd39653-d908-45fd-b705-d6c0a9a470bd_1708389879.3619761.png)

---


# Approaches
(Also explained in the code)

#### ***Approach 1(Using Vectors)***
1. Will iterate over the nums and will put elements in the v vector(size of n+1).
![Screenshot 2024-02-20 062119.png](https://assets.leetcode.com/users/images/cd248f54-0371-448e-a8ef-5edb1139ced1_1708390307.8573344.png)

1. At last will iterate in v and  will return index of the element which is still -1. 

# Complexity
- Time complexity:
   $$O(n)$$
    

- Space complexity:
   $$O(n)$$
    


# Code
```C++ []
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        vector<int>v(n+1,-1);
        for(int i =0;i<nums.size();i++){
            v[nums[i]] = nums[i];
        }
        for(int i =0;i<v.size();i++){
            if(v[i]==-1)return i;
        }
        return 0;
    }
};



```
```Java []
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int[] v = new int[n+1];
        Arrays.fill(v, -1);
        for(int i = 0; i < nums.length; i++) {
            v[nums[i]] = nums[i];
        }
        for(int i = 0; i < v.length; i++) {
            if(v[i] == -1) return i;
        }
        return 0;
    }
}


```
```python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v = [-1] * (n + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0


```
```javascript []
var missingNumber = function(nums) {
    let n = nums.length;
    let v = new Array(n+1).fill(-1);
    for(let i = 0; i < nums.length; i++) {
        v[nums[i]] = nums[i];
    }
    for(let i = 0; i < v.length; i++) {
        if(v[i] == -1) return i;
    }
    return 0;
};



```
---

#### ***Approach 2(XOR Operation)***
1. **XOR operation we should be known:**
![Screenshot 2024-02-20 063237.png](https://assets.leetcode.com/users/images/3eab0e5d-a8aa-4318-b849-42b077d76540_1708391021.2734692.png)

1. We will xor each number present in the nums to itself.
1. Then will xor it with every number present in the range [0,n].
![Screenshot 2024-02-20 063312.png](https://assets.leetcode.com/users/images/80de0aa9-e157-4797-a72f-d8e3ddede584_1708391030.4057143.png)

# Complexity
- Time complexity:
   $$O(n)$$
    

- Space complexity:
   $$O(1)$$
    


# Code
```C++ []
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int ans =0;
        for(int i =1;i<=n;i++){
            ans = ans ^ i;
        }
        for(int i =0;i<nums.size();i++){
            ans= ans^nums[i];
        }
        return ans;
    }
};



```
```Java []
public class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            ans = ans ^ i;
        }
        for (int i = 0; i < nums.length; i++) {
            ans = ans ^ nums[i];
        }
        return ans;
    }
}


```
```python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans


```
```javascript []
var missingNumber = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        ans ^= i;
    }
    for (let i = 0; i < nums.length; i++) {
        ans ^= nums[i];
    }
    return ans;
};



```
---

#### ***Approach 3(Sum of all elememnts)***
1. sum of all elements in the range[0,n].
1. sum of nums.
1. If we subtrate both we will get the missing number
![Screenshot 2024-02-20 063822.png](https://assets.leetcode.com/users/images/4fe083ce-7da9-4f12-8228-663704ece990_1708391316.4567716.png)


# Complexity
- Time complexity:
   $$O(n)$$
    

- Space complexity:
   $$O(1)$$
    


# Code
```C++ []
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int n = nums.size();
        int Tsum = (n*(n+1))/2;
        return  Tsum - accumulate(nums.begin(),nums.end(),0);
        
    }
}; 



```
```Java []


class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int Tsum = (n * (n + 1)) / 2;
        int actualSum = Arrays.stream(nums).sum();
        return Tsum - actualSum;
    }
}


```
```python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return Tsum - actual_sum


```
```javascript []
var missingNumber = function(nums) {
    const n = nums.length;
    const Tsum = (n * (n + 1)) / 2;
    const actualSum = nums.reduce((acc, num) => acc + num, 0);
    return Tsum - actualSum;
};



```
---
#### ***Approach 4(Sorting)***
1. cases after sorting
![Screenshot 2024-02-20 070914.png](https://assets.leetcode.com/users/images/e43b7f6a-8da1-4b27-81f1-33b8a4b7d5c8_1708393182.210457.png)

1. If starting number isnt 0 after sorting which implies there is no missing number.
![Screenshot 2024-02-20 070919.png](https://assets.leetcode.com/users/images/8fbac9d1-0a21-4ba0-9920-57d46ef87aba_1708393189.7561924.png)

1. If last number is missing then the index will never match with the last element.
![Screenshot 2024-02-20 070925.png](https://assets.leetcode.com/users/images/5cbc665a-9bfa-4b5b-b3e7-23f6cc05ca22_1708393197.6987033.png)

1. If any number other than 1st and last is missing it, then return i.
![Screenshot 2024-02-20 070929.png](https://assets.leetcode.com/users/images/1dfff08b-b9de-4939-8c21-499b38823ad8_1708393205.0993302.png)


# Complexity
- Time complexity:
   $$O(nlogn)$$
    

- Space complexity:
   $$O(1)$$
    


# Code
```C++ []
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        //case 1
        if(nums[0] != 0)return 0;
        //case 2 
        if(nums[n-1] != n)return n;
        for(int i =1;i<nums.size();i++){
            if(nums[i] != i){
            //case 3
            return i;
            }
        }
        return 0;
    }
};


```
```Java []
import java.util.Arrays;

class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        
        // Case 1
        if (nums[0] != 0) return 0;
        
        // Case 2
        if (nums[n - 1] != n) return n;
        
        // Case 3
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != i) return i;
        }
        
        return 0;
    }
}



```
```python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Case 1
        if nums[0] != 0:
            return 0
        
        # Case 2
        if nums[-1] != n:
            return n
        
        # Case 3
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        
        return 0


```
```javascript []
var missingNumber = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    
    // Case 1
    if (nums[0] !== 0) return 0;
    
    // Case 2
    if (nums[n - 1] !== n) return n;
    
    // Case 3
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== i) return i;
    }
    
    return 0;
};




```
---





# DO GIVE IT A LIKE IF THAT WAS HELPFUL\uD83E\uDEE1\uD83D\uDC47

---
---


---

</details>
