# First Missing Positive

| Field | Value |
|-------|-------|
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Language** | python |
| **Solved On** | September 29, 2026 |
| **Tags** | Array, Hash Table |
| **Link** | [View Problem](https://leetcode.com/problems/first-missing-positive/) |
| **Runtime** | 75 ms |
| **Memory** | 20 MB |

## Problem Description

<p>Given an unsorted integer array <code>nums</code>. Return the <em>smallest positive integer</em> that is <em>not present</em> in <code>nums</code>.</p>

<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


##  Top Community Optimal Approach

<details>
<summary>Click to expand</summary>

**Title**: Hard❌ |Easy✅ || Positioning Elements at correct index
**Author**: [@CS_MONKS](https://leetcode.com/CS_MONKS/)
**Upvotes**: 285 👍
**Link**: [View Original Post](https://leetcode.com/problems/first-missing-positive/solutions/4925619/)

---

Master array manipulation and algorithmic problem-solving by finding the smallest missing positive integer efficiently in this challenge!
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires finding the smallest positive integer that is not present in an unsorted integer array. To achieve this efficiently, we can utilize the fact that the answer lies within the range [1, n+1], where n is the size of the array. By rearranging the elements of the array, we can position each positive integer i at index i-1. Then, we iterate through the array to find the first index i where nums[i] != i+1, indicating the missing positive integer is i+1.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Iterate through the array and place each positive integer i at index i-1 if possible. This ensures that the element nums[i] == i+1 if it exists in the array.
2. Iterate through the array again to find the first index i where nums[i] != i+1. Return i+1 as the smallest missing positive integer.
3. If all numbers from 1 to n are present in the array, return n+1 as the result.

# Dry run

let\'s do a dry run of the given array [3, 4, -1, 1] 

Iteration 1:
Current array: [3, 4, -1, 1]
For element 3 (at index 0), swap it with the element at index 2 because 3 should be at index 2  swap(3,-1).
Updated array: [-1, 4, 3, 1]
now since -1 is out of range [1, n]
we will skip inner loop

Iteration 2:
Current array: [-1, 4, 3, 1]
For element 4 (at index 1), swap it with the element at index 3 because 4 should be at index 3 swap(4,1).
Updated array: [-1, 1, 3, 4]
now 1 is in the range [1, n] , 1 is not at it correct index
so swap(1,-1)
Updated array: [1, -1, 3, 4]

Iteration 3:
now 3 is present at correct index so skip this loop

Iteration 4:
now 4 is present at correct index so skip this loop
Final check:

We traverse the array again to find the smallest missing positive integer.
The first missing positive integer is 2 since it\'s not present in the array.
So, the smallest missing positive integer in the array [3, 4, -1, 1] is 2.

# Complexity
- Time complexity:O(n), where n is the size of the array. Both iterations through the array take linear time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1). The algorithm uses only a constant amount of extra space, regardless of the size of the input array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```c++ []
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n= size(nums);
       
        for(int i=0;i<n;i++){
            int x=nums[i]; // x = current element
            
        // x>=1 && x<=n : to check if x is in range[1, n]
        // x != i+1 : skip if at index i correct element is present.
        // nums[x-1]!=x: skip if at index x-1 correct element is present
            while(x>=1 && x<=n && x!=i+1 && nums[x-1]!=x){
                swap(nums[x-1],nums[i]);
                x=nums[i];
            }
        }


        for(int i=0;i<n;i++){
            if(nums[i] == i+1)continue;
                return i+1;       
            
        }
        
        return n+1;
    }
};
```

```python3 []
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1

```
```java []
class Solution {
    // Function to swap elements in the array
    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        // Place each positive integer i at index i-1 if possible
        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            }
        }
        
        // Find the first missing positive integer
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        // If all positive integers from 1 to n are present, return n + 1
        return n + 1;
    }
}

}

```
```javascript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    // Function to swap elements in the array
    const swap = (arr, i, j) => {
        [arr[i], arr[j]] = [arr[j], arr[i]];
    };
    
    const n = nums.length;
    
    // Place each positive integer i at index i-1 if possible
    for (let i = 0; i < n; i++) {
        while (nums[i] > 0 && nums[i] <= n && nums[i] !== nums[nums[i] - 1]) {
            swap(nums, i, nums[i] - 1);
        }
    }
    
    // Find the first missing positive integer
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) {
            return i + 1;
        }
    }
    
    // If all positive integers from 1 to n are present, return n + 1
    return n + 1;
};

```
In complete code inner loop will not run more than n time. In each iteration of inner loop we are placing one element at it correct position. So if inner loop run n times all element will get positioned at correct index. After that inner loop will not run any more
So time complexity of first loop in worst case O(2*n)==O(n)

# My Friends try these two \uD83D\uDC79
```c++ []
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n=size(nums);
        bool onepresent=false;
        // if one is missing return one 
        for(int i=0;i<n;i++){
            if(nums[i]==1)onepresent=true;
            if(nums[i]<=0 || nums[i]>n)nums[i]=1;
        }
        if(onepresent==false)return 1;
        nums.push_back(1);
        
        // if x is present make element at nums[x] negative
        for(int i=0;i<n;i++){
            int ind=abs(nums[i]);
            if(nums[ind]>0)nums[ind]=-1*nums[ind];
        }
         
        // if a index is not negative that mean that element   was  not present in array    
        for(int i=1;i<=n;i++){
            if(nums[i]>0)return i;
        }
        return n+1;
    }
};
```
```c++ []
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = size(nums);
        for (int j = 0; j < 5; j++)
            for (int i = 0; i < n; i++) {
                int x = nums[i];
                if (x >= 1 && x <= n) {
                    swap(nums[x - 1], nums[i]);
                }
            }

        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return n + 1;
    }
};
```


![upvote.jpg](https://assets.leetcode.com/users/images/32bf116a-dcff-4a1c-b18c-3dd53b2f1124_1711412678.8323216.jpeg)





</details>
