class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        out=ListNode(0)
        out.next=head
        prev=out
        curr=head
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
                    
            curr=curr.next
                
        return out.next
