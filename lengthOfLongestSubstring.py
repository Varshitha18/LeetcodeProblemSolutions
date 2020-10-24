#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_so_far = 0
        hm = {}
        start = 0
        for i in range(len(s)):
            if(s[i] in hm):
                start = max(hm[s[i]] + 1, start)
            max_so_far = max(max_so_far, i-start+1)
            hm[s[i]] = i
        return max_so_far


'''
Algorithm:
    -> Iterate through the string, if the current character is already present in dictionary, update the start of the required substring
    -> If current character does not exist in dictionary, add the character-index as key-value pairs into it, else update the value of character.
    -> Update the length of the maximum length substring


Complexities:
    Space - O(n)
    Time - O(n)
'''
