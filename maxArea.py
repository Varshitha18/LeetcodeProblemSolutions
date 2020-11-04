#https://leetcode.com/problems/container-with-most-water/

#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        ans = 0
        end = len(height)-1
        while(start != end):
            if(height[start] < height[end]):
                area = height[start]*(end - start)
                start += 1
            else:
                area = height[end]*(end - start)
                end -= 1
            if(ans < area):
                ans = area
        return ans


'''
Algorithm:
    -> A two pointer approach is used here.
    -> Place two pointers, one at the start and another at the end of the array.
    -> Calculate the area between the two pointers and move the pointer pointing to the smaller of the two heights by one distance on the x-axis. This is because the smaller height determines the amount of water that can be stored.
    -> Update the maximum area with each iteration.
    -> Return the maximum area.

Complexity:
    Space - O(1)
    Time - O(n) where n is length of array.

'''






