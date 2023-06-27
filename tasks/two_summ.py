#! /usr/bin/env python3 

""" 
TASK 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

list_nums = [1, 2, 4, 5]
target = 3

def two_summ_one(list_nums, target):
    """Bad"""

    lenght_list = len(list_nums)
    for i in range(lenght_list - 1):
        for j in range(i + 1, lenght_list):
            if list_nums[i] + list_nums[j] == target:
                return [i, j]
    return []

def two_sum_with_dict(list_nums, target):
    map_nums = {}
    lenght_list = len(list_nums)
    for i in range(lenght_list):
        map_nums[list_nums[i]] = i
    for j in range(lenght_list):
        solv = target - list_nums[j]
        if solv in map_nums and map_nums[solv] != j:
            return [j, map_nums[solv]]
    return []

print(two_sum_with_dict(list_nums, target))

            



