## Leetcode

### Resources

Bit manipulation: https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/

### [Problem 1. Two Sum](https://leetcode.com/problems/two-sum/)

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### [Problem 2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

#### [Problem 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string s, find the length of the longest substring without repeating characters.

```
input : "abcabcbb"
output : 3
Explanation : The answer is "abc", with the length of 3.
```

```
input : "bbbbb"
output : 1
Explanation : The answer is "b", with the length of 1.
```

### [Problem 4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

hint: sort the array and find the median

### [Problem 5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string s, return the longest palindromic substring in s.

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Explanation: "aba" is a palindrome, "bab" is a substring.
```

### [Problem 6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

Given a string s and an integer numRows, convert s into a zigzag pattern. More formally, convert s into a rows x numRows grid by placing each character in s in one of the rows, going from top to bottom row by row. Then, read the zigzag pattern from left to right. The characters in each row are read from left to right and the characters are concatenated to form a string.

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R
```

### [Problem 7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

```
Input: x = 123
Output: 321
```

### [Problem 8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

```
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
Step 3: "42" ("42" is read in)
              ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
```

### [Problem 9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Given an integer x, return true if x is a palindrome integer.

```
Input: x = 121
Output: true

Explanation: From left to right, it reads 121. From right to left, it becomes 121. Therefore it is a palindrome.
```

### [Problem 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

A container with water is given. The container can be filled with water. The container has a length and width. The container can hold water up to the height of the container. Find two vertical lines, which together with the x-axis forms a container, such that the container contains the most water.

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### [Problem 12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

Given an integer, convert it to a roman numeral.

```
Input: num = 3
Output: "III"

Explanation: The number 3 is written in Roman numerals as "III".
```

### [Problem 13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Given a roman numeral, convert it to an integer.

```
Input: s = "III"
Output: 3
Explanation: The numeral III is a representation of the number 3.
```

### [Problem 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

Explanation: The longest common prefix is "fl".
```

### [Problem 15. 3Sum](https://leetcode.com/problems/3sum/)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: The triplets are: [-1, 0, 1], [-1, -1, 2]
```

### [Problem 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

```
Input: s = "()"
Output: true
```

### [Problem 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Explanation: The linked list is [1,1,2,3,4,4].
```

### Problem 23. Merge k Sorted Lists (https://leetcode.com/problems/merge-k-sorted-lists/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]

Output: [1,1,2,3,4,4,5,6]

Explanation: The linked list is [1,1,2,3,4,4,5,6].
```

### Problem 26. Remove Duplicates from Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```

### Problem 27. Remove Element (https://leetcode.com/problems/remove-element/)

Given an integer array nums and an integer val, remove all occurrences of val "in nums" in-place. The relative order of the elements may be changed.

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
```

### [Problem 28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

```
Input: haystack = "hello", needle = "ll"
Output: 2

Explanation: The first occurrence of "ll" is at index 2.
```

### Problem 29. Divide Two Integers (https://leetcode.com/problems/divide-two-integers/)

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
```

### [Problem 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Explanation: The target value is present at index 4.
```

### [Problem 34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Explanation: The value 8 is present at index 3 and 4.
```

### [Problem 35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

A sorted array of distinct integers is given. Find the index of the target value. If the target value is not found, return the index where it would be if it were inserted in order.

```
Input: nums = [1,3,5,6], target = 5
Output: 2
Explanation: 5 exists in nums and its index is 2.
```

### [Problem 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### [Problem 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: The groupings are as follows:
"ate", "eat", and "tea" are all anagrams of each other, so they all belong to the same group.
"nat" and "tan" are anagrams of each other, so they all belong to the same group.
"bat" is not an anagram of any other word, so it its own group.
```

### [Problem 50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

```
Input: x = 2.00000, n = 10
Output: 1024.00000
Explanation: 2^10 = 1024.
```

### [Problem 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Solved with 3 different approaches

1. Brute Force
2. Divide and Conquer
3. Kadane's Algorithm

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### [Problem 55. Jump Game](https://leetcode.com/problems/jump-game/)

Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you can reach the last index.

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### [Problem 58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

### [Problem 66. Plus One](https://leetcode.com/problems/plus-one/)

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

```
Input: digits = [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123. Incrementing by one gives 124.
```

### [Problem 67. Add Binary](https://leetcode.com/problems/add-binary/)

```
Input: a = "11", b = "1"
Output: "100"
Explanation: The sum of binary strings 11 and 1 is 100.
```

### [Problem 69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Given a non-negative integer x, compute and return the square root of x.

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.
```

### [Problem 75. Sort Colors](https://leetcode.com/problems/sort-colors/)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Explanation: The output is the array in the correct order.
```

### [Problem 78. Subsets](https://leetcode.com/problems/subsets/)

Given an integer array nums of unique elements, return all possible subsets (the power set).

```
Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### [Problem 80 Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
```

### [Problem 83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

```
Input: head = [1,1,2]
Output: [1,2]

Explanation: The linked list is 1 -> 1 -> 2. After removing the duplicates, it is now 1 -> 2.
```

#### [Problem 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

### [Problem 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

```
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation: The inorder traversal is [1,3,2].
```

hint: sort the array from the end

### [Problem 100. Same Tree](https://leetcode.com/problems/same-tree/)

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
Explanation: The two binary trees are the same.
```

### [Problem 101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

```
Input: root = [1,2,2,3,4,4,3]
Output: true
Explanation: The binary tree is symmetric.
```

### [Problem 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation: The level order traversal of the binary tree is [[3],[9,20],[15,7]].
```

### [Problem 103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

```
Input: root = [3,9,20,null,null,15,7]

Output: [[3],[20,9],[15,7]]
Explanation: The zigzag level order traversal of the binary tree is [[3],[20,9],[15,7]].
```

### [Problem 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth.

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation: The maximum depth is 3.
```

### [Problem 107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

```
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Explanation: The bottom-up level order traversal of the binary tree is [[15,7],[9,20],[3]].
```

### [Problem 110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

Given a binary tree, determine if it is height-balanced.

```
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: The binary tree is height-balanced.
```

### [Problem 111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

Given a binary tree, find its minimum depth.

```
Input: root = [3,9,20,null,null,15,7]
Output: 2
Explanation: The minimum depth is 2.
```

### [Problem 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

### [Problem 122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

### [Problem 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### [Problem 128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### [Problem 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### [Problem 142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

```
Input: head = [3,2,0,-4], pos = 1
Output: [2]
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### [Problem 143. Reorder List](https://leetcode.com/problems/reorder-list/)

Given the head of a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Explanation: The reordered list is [1,4,2,3].
```

### [Problem 146. LRU Cache](https://leetcode.com/problems/lru-cache/)

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

```
Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation: The LRU cache is shown as below:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

### [Problem 151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string s, reverse the order of the words.

```
Input: s = "the sky is blue"
Output: "blue is sky the"
Explanation: The words are reversed.
```

### [Problem 154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 7 times.

```
Input: nums = [4,5,6,7,0,1,4]
Output: 0
Explanation: The original array was [0,1,4,4,5,6,7] rotated 4 times.
The smallest element is 0.
```

### [Problem 160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: [8,4,5]
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
```

### [Problem 167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

(similar to problem 1)
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### [Problem 169. Majority Element](https://leetcode.com/problems/majority-element/)

Given an array nums of size n, return the majority element.

```
Input: nums = [3,2,3]
Output: 3
Explanation: The majority element is 3.
```

### [Problem 189. Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: After rotating the array by 3 steps to the right, we get [5,6,7,1,2,3,4].
```

### [Problem 191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

### [Problem 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation: The right view of the binary tree is [1,3,4].
```

### [Problem 202. Happy Number](https://leetcode.com/problems/happy-number/)

Write an algorithm to determine if a number n is happy.

```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

### [Problem 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Explanation: The linked list is 1 -> 2 -> 3 -> 4 -> 5. After reversing the linked list, the linked list becomes 5 -> 4 -> 3 -> 2 -> 1.
```

### [Problem 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

### [Problem 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Given an integer array nums and an integer k, return the kth largest element in the array.

```

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Explanation: The 2nd largest element is 5.

```

### [Problem 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```
Input: nums = [1,2,3,1]
Output: true
```

### [Problem 219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

### [Problem 223. Rectangle Area](https://leetcode.com/problems/rectangle-area/)

Find the total area covered by two rectilinear rectangles in a 2D plane. Each rectangle is defined by its bottom left corner and top right corner.

```
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
```

### [Problem 225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

```
Input: ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output: [null, null, null, 2, 2, false]
Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

### [Problem 232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

```
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 1, 1, false]

Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

### [Problem 234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given the head of a singly linked list, return true if it is a palindrome.

```
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
```

### [Problem 237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

### [Problem 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

```

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: The array of the products of all other elements is [24,12,8,6]. The product of all the elements of nums is 24. So, for each index i in nums, we have nums[i] = 24 / nums[i].

```

### [Problem 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings s and t , write a function to determine if t is an anagram of s.

```

Input: s = "anagram", t = "nagaram"
Output: true
Explanation: Both s and t contain all the same letters, in the same frequency, so they are anagrams.
```

### [Problem 268. Missing Number](https://leetcode.com/problems/missing-number/)

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

### [Problem 274. H-Index](https://leetcode.com/problems/h-index/)

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: The researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations.
```

### [Problem 295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

```
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output: [null, null, null, 1.5, null, 2.0]

Explanation: MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### [Problem 328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Explanation: The first node is odd and remaining are even. The odd nodes are [1,3,5] and even nodes are [2,4].
```

### [Problem 338. Counting Bits](https://leetcode.com/problems/counting-bits/)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
number --> binary --> count of 1
0      -->   000  -->       0
1      -->   001  -->       1
2      -->   010  -->       1
3      -->   011  -->       2
4      -->   100  -->       1
5      -->   101  -->       2
```

### [Problem 344. Reverse String](https://leetcode.com/problems/reverse-string/)

Write a function that reverses a string. The input string is given as an array of characters s.

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

### [Problem 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

```

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. In this case, the answer is [1,2] because both 1 and 2 appear twice, and 1 comes before 2.

```

### [Problem 380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Design a data structure that supports all following operations in average O(1) time.

- insert(val): Inserts an item val to the set if not already present.
- remove(val): Removes an item val from the set if present.
- getRandom: Returns a random element from the current set of elements. Each element must have the same probability of being returned.

### [Problem 383. Ransom Note](https://leetcode.com/problems/ransom-note/)

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
Explanation: ransomNote is "aa" and magazine is "aab", so ransomNote can be constructed from magazine.
```

### [Problem 392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

```
Input: s = "abc", t = "ahbgdc"
Output: true

Explanation: The string "abc" is a subsequence of "ahbgdc".
```

### [Problem 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### [Problem 438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

### [Problem 445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

```
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explanation: 7243 + 564 = 7807
```

### [Problem 451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string. If there are multiple answers, return any of them.

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once. The answer can be "eetr" as well.
```

### [Problem 506. Relative Ranks](https://leetcode.com/problems/relative-ranks/)

Given an integer array score of size n, return the relative ranks of the athletes. The relative ranks are the positions of the athletes in the leaderboard.

```
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The athletes are ranked as follows:

Gold Medal: Score 10 is the highest.
5: Score 9.
Bronze Medal: Score 8.
Silver Medal: Score 4.
```

### [Problem 513. Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/)

Given the root of a binary tree, return the leftmost value in the last row of the tree.

```
Input: root = [2,1,3]
Output: 1
Explanation: The tree is:
  2
 / \
1   3
```

### [Problem 525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

### [Problem 535. Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl)

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

```
Input: longUrl = "https://leetcode.com/problems/design-tinyurl"
Output: "http://tinyurl.com/4e9iAk"
```

### [Problem 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Given the root of a binary tree, return the length of the diameter of the tree.

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

### [Problem 622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

```
Input: ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output: [null, true, true, true, false, 3, true, true, true, 4]
```

### [Problem 658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1

```

### [Problem 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

```
Input: ["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

### [Problem 704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

### [Problem 706. Design HashMap](https://leetcode.com/problems/design-hashmap/)

Design a HashMap without using any built-in hash table libraries.

```
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
```

### [Problem 725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

```
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.

The last element output[4] is null, but it's string representation as a ListNode is [].

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are larger than the later parts.
```

### [Problem 771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

```

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Explanation: All the stones are jewels, you have 3 jewels.

```

### [Problem 786. K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/)

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

```
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
```

### [Problem 796. Rotate String](https://leetcode.com/problems/rotate-string/)

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

```
Input: s = "abcde", goal = "cdeab"
Output: true

Input: s = "abcde", goal = "abced"
Output: false
```

### [Problem 876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Given the head of a singly linked list, return the middle node of the linked list.

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

### [Problem 881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

```
Input: people = [3,2,2,1], limit = 3
Output: 3

Explanation: 3 boats (1, 2), (2) and (3)
```

### [Problem 938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

```

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

```

### [Problem 997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge. If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

```

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
Explanation: The town judge is the person labeled 3. Everyone trusts 3 except for 3, and no one trusts 3.

```

Hint:

# The idea is to calculate incoming and outgoing edges

# for each person in the trust. Judge is a a person with n-1 incming edge and 0 outgoing edge.

explanation: https://www.youtube.com/watch?v=QiGaxdUINJ8

### [Problem 1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

```

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move. The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

### [Problem 1209. Remove all adjacent Duplicates II ]

```

Input : s = "deeedbbcccbdaa", k = 3
Output : "aa"
Explanation :
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

```

### [Problem 1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)

Given the root of a binary tree, return the sum of values of its deepest leaves.

```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```

### [Problem 1337. The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)

Given a m \* n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

```
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].
```

### [Problem 1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

```
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
```

### [Problem 1464. Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

```
Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
```

### [Problem 1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

```
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

### [Problem 1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.

```

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

```

### [Problem 1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

```

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

```

#### [Problem 1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

```

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:

- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
  You can take all the boxes of the first and second types, and one box of the third type.
  The total number of units will be = (1 _ 3) + (2 _ 2) + (1 \* 1) = 8.

```

#### [Problem 1859. Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)

```

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

```

### [Problem: 1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

```

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

```

### [Problem 2006. Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/)

```
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
```

### [Problem 2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/)

```
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.s
```

### [Problem: 2220. (Easy): Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/)

```

You are given two numbers a and b. You need to find the number of bits you need to flip to convert a to b. Note: All given integers are in binary form.

Input: a = 10, b = 20
Output: 4
Explanation:
a = 01010
b = 10100
As we can see, the bits of a that need to be flipped are 01010. If we flip these bits, we get 10100, which is b. Hence, the number of bits that need to be flipped is 4.


X >> Y means x is shifted to the right by y bits. This is equivalent to dividing x by 2^y.
e.g 8 >> 1 = 4 (1000 >> 1 = 0100)

```

### [Problem 2265. (Medium) Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/)

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note: The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

A subtree of root is a tree consisting of root and all of its descendants.

```
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
```

### [Problem 2331. (Easy): Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/description/)

```
Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
```

### [Problem 2236. Root equals sum of children](https://leetcode.com/problems/root-equals-sum-of-children/description/)

Given a binary tree root, return whether the sum of all leaves is equal to the sum of all non-leaf nodes.

```
Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
```

### [Problem 2487. (Easy): Find the Score of All Prefixes](https://leetcode.com/problems/find-the-score-of-all-prefixes/description/)

Given an array of integers nums, you are asked to calculate the score of all prefixes of the array. The score of a prefix is defined as the sum of the elements of the prefix multiplied by the length of the prefix.

```
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.

- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
```

### [Problem 2500. (Easy) Delete Greatest Value in Each Row]

Given a 2D integer array matrix, you need to delete the greatest value in each row. Return the sum of all the deleted values.

```
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.
```

### [Problem 2640. (Medium) Find the score of all prefixes](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array)

```

Input: nums = [2,3,7,5,10]
Output: [4,10,24,36,56]
Explanation:
For the prefix [2], the conversion array is [4] hence the score is 4
For the prefix [2, 3], the conversion array is [4, 6] hence the score is 10
For the prefix [2, 3, 7], the conversion array is [4, 6, 14] hence the score is 24
For the prefix [2, 3, 7, 5], the conversion array is [4, 6, 14, 12] hence the score is 36
For the prefix [2, 3, 7, 5, 10], the conversion array is [4, 6, 14, 12, 20] hence the score is 56

```

### [Problem 2816. (Medium) Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list)

```
Input: head = [1,2,3]
Output: [2,4,6]
Explanation: The linked list is 1 -> 2 -> 3. After doubling the linked list, the linked list becomes 2 -> 4 -> 6.
```

### [Problem 2974. (Easy) Minimum Number Game] (https://leetcode.com/problems/minimum-number-game)

```
Input: nums = [5,4,2,3]
Output: [3,2,5,4]
Explanation: In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].
```

### [Problem 3075. (Medium) Maximum Happiness of Selected Children](https://leetcode.com/problems/maximum-happiness-of-selected-children)

```
Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.
```

### [Problem 3110. (Easy) Score of a String](https://leetcode.com/problems/score-of-a-string)

```
Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13
```

### Problem 3114. (Easy) Find the Score of All Prefixes of a String

```
Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".
```

### Problem 3120. Count the Number of Special Characters I

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

```
Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.
```

### Problem 3121. Count the Number of Special Characters II

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

### Problem 3136. (Easy) Valid Word

A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.

```
Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.
```
