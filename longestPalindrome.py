#https://leetcode.com/problems/longest-palindromic-substring/

#Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        maxi = 1
        ans_start = 0
        for i in range(n):
            dp[i][i] = True
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                if(s[start] == s[end]):
                    if(end - start == 1 or dp[start+1][end-1]):
                        dp[start][end] = True
                        if(maxi < end - start+1):
                            maxi = end - start + 1
                            ans_start = start
        return s[ans_start: ans_start+maxi]

'''
Algorithm:
    -> A DP(dynamic programming) approach is used for this problem.
    -> A 2D array of size nxn where n is length of the word is taken. As each single letter is a palindrome in itself, the array is initialised with 'True' where the row and column indexes are same and rest with 'False'.
    -> Two nested for loops are used, one for looping through various lengths and other for looping through various start indices. 
    -> If the character at start index is same as that at the end index of the substring being considered:
       - If the substring in between the indices is a palindrome, then the current substring is also a palindrome.    -> Keep updating the maximum length and start index of substring whenever the previous condition is satisfied.    -> Return the substring from the stored start index for the stored maximum length.



Complexity:
    Space - O(n^2) where n is length of string
    Time - O(n^2)

'''
