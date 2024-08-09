# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = head
        fast = head
        slow = head
        i = 0

        while fast:
            if i <= n:
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
            i += 1

        if i == n and i >= 2:
            res = res.next
        elif i == n and i == 1:
            res = None
        else:
            slow.next = slow.next.next

        return res


nums = [1, 2, -1, 2]
print(nums)
nums = nums.sort()
print(nums)
