'''
Sliding Window: Use two pointers to represent a continuous section of an array or string.
Instead of recalculating every subarray, we expand and shrink a window based on a certain condition.

Usually:
left = start of the window
right = end of the window

There are two main types:
1. Fixed-size Sliding Window: The window always has the same size.

Find the maximum sum of any 3 consecutive numbers.

Example 1:
Input: nums = [2,1,5,1,3,2], k = 3
Output: 9

def max_sum_brute_force(nums, k):
    max_sum = float('-inf') 
    for i in range(len(nums) - k + 1): # o(n)
        curr_sum = 0
        for j in range(i, i + k): # o(k)
            curr_sum += nums[j]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# t.c: o(n * k)
# s.c: o(1)

def max_sum_optimized(nums, k):
    curr_sum = sum(nums[:k]) # 0 -> 2
    max_sum = curr_sum
    i = 0
    for j in range(k, len(nums)):
        curr_sum -= nums[i]
        curr_sum += nums[j]
        i += 1
        
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

2. Variable-size Sliding Window: The window grows and shrinks depending on a condition.

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.

def longest_substring(s):
    l = 0
    longest_len = 0
    seen = set()

    for r in range(len(s)):
        char = s[r]

        while char in seen:
            seen.remove(s[l])
            l += 1

        seen.add(char)
        longest_len = max(longest_len, r - l + 1)
    
    return longest_len

# t.c: o(n)
# s.c: o(n)
'''