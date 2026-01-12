# Day 25 – LeetCode Practice

## Problem Solved:
**Unique Paths II (LeetCode 63) – Medium**

## Problem Statement:
Given a `m x n` grid filled with obstacles (represented by 1) and empty spaces (0), find how many unique paths exist from the **top-left corner** to the **bottom-right corner**. You can only move **down** or **right**, and cannot move through obstacles.

## Approach / What I Learned:
- Learned how to handle **2D dynamic programming** problems.
- Practiced building a **DP table** where each cell represents the number of ways to reach that cell.
- Learned to **handle edge cases**, like when the starting or ending cell has an obstacle.
- Improved understanding of **grid traversal** and how obstacles affect path counts.

### Steps:
1. Create a DP matrix of size `m x n`.
2. Initialize the starting point: if there is no obstacle, set it to 1.
3. For each cell in the grid:
   - If it's an obstacle, set DP value = 0.
   - Else, DP value = sum of paths from top and left cells.
4. Result is the value in the bottom-right cell.

## Status:
✅ Problem solved successfully

#Python #LeetCode #DynamicProgramming #ProblemSolving #365DaysOfCoding #LearningEveryday