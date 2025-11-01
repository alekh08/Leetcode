# Description
# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.


# Example 1:

# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]

#-------------------------------------------------------------- Solution -------------------------------------------------------------- #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num=set(nums)
        dum=ListNode(0)
        dum.next=head
        curr=dum
        # traverse and remove nodes whose val are in num
        while curr.next:
            if curr.next.val in num:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dum.next
