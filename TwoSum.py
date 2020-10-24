#https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if(nums[i] not in hm):
                hm[nums[i]] = i
            if((target - nums[i]) in hm and hm[target-nums[i]] != i):
                return [i, hm[target-nums[i]]]

'''
Algorithm:
    -> Store each element of nums in dictionary if it does not already exist.
    -> Check if the required number to add to sum up to the target already exists in the dictionary:
        - if it exists, required pair is found
        - if it does not exist, continue iterating

Complexity:
    Space - O(n) where n is number of elements
    Time - O(n)
'''
