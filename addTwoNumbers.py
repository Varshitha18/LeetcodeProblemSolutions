#https://leetcode.com/problems/add-two-numbers/

#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = head = ListNode(-1)
        carry = 0
        while(l1 is not None or l2 is not None):
            fdata = l1.val if l1 else 0
            sdata = l2.val if l2 else 0
            sumi = fdata + sdata + carry
            carry = sumi//10
            head.next = ListNode(sumi%10)
            head = head.next
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        if(carry > 0):
            head.next = ListNode(carry)
        return curr.next


'''
Algorithm:
    -> While either of the numbers exist:
       - take the node value if number exists or value as 0
       - add the node values along with carry and store the sum
       - update tens place of sum in prev step as carry
       - create a new node with units place of calculated sum
    -> if carry is not 0:
        create a new node with carry value


Complexity:
    -> Space - O(1)
    -> Time - O(n)
'''
