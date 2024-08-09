# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         plus_one = 0
#         res = ListNode()
#         ptr = res

#         def get_val(n):
#             if not n:
#                 return 0
#             else:
#                 return n.val

#         def get_next(n):
#             if not n:
#                 return None
#             else:
#                 return n.next

#         while l1 or l2:

#             if get_val(l1) + get_val(l2) + plus_one >= 10:
#                 ptr.val = get_val(l1) + get_val(l2) + plus_one - 10
#                 plus_one = 1
#             else:
#                 ptr.val = get_val(l1) + get_val(l2) + plus_one
#                 plus_one = 0

#             l1 = get_next(l1)
#             l2 = get_next(l2)

#             if not l1 and not l2 and plus_one == 0:
#                 ptr.next = None
#             elif not l1 and not l2 and plus_one == 1:
#                 ptr.next = ListNode(val=1)
#             else:
#                 ptr.next = ListNode()
#                 ptr = ptr.next

#         return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        carry, total = 0, 0
        dummy = ListNode()
        res = dummy

        while l1 or l2 or carry:

            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            total = total % 10

            dummy.next = ListNode(total)
            dummy = dummy.next

        return res.next
