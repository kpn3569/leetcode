# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(0)
        t = 0
        tt = 0
        sk=s
        while l1 and l2:
            tt = (t + l1.val + l2.val) % 10
            t = (t + l1.val + l2.val) // 10
            l1.val = tt
            s.next=l1
            l1 = l1.next
            l2 = l2.next
            s=s.next

        if l1:
            while l1:
                tt = (t + l1.val) % 10
                t = (t + l1.val) // 10
                l1.val = tt
                s.next=l1
                s=s.next
                if l1.next is None:
                    break
                l1 = l1.next

        if l2:
            while l2:
                tt = (t + l2.val) % 10
                t = (t + l2.val) // 10
                l2.val = tt
                s.next=l2
                s=s.next
                if l2.next is None:
                    break
                l2 = l2.next
        if t == 1:
            ss = ListNode(t)
            s.next = ss

        return sk.next
