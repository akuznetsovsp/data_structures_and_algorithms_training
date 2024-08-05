# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        res = []
        # print(head.val, head.next)

        def recursive_store_value(l):
            if l.next == None:
                res.append(l.val)
                return
            else:
                res.append(l.val)
                return recursive_store_value(l.next)

        recursive_store_value(head)
        i = 0
        j = len(res) - 1

        while i <= j:
            if res[i] == res[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
