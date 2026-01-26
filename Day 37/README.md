Day 37 – #365DaysOfLeetCode
LeetCode 268 – Missing Number (Easy)

Problem

Given an array containing n distinct numbers in the range [0, n], return the only number that is missing from the array.
Approach

Calculate the expected sum of numbers from 0 to n using the formula: expected_sum = n * (n + 1) / 2
Find the actual sum of the array
Missing number = expected_sum - actual_sum

Complexity

Time Complexity: O(n)
Space Complexity: O(1)
