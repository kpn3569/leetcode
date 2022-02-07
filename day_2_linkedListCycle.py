
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        s=f=head
        while s and f:
            s=s.next
            if f.next is not None:
                f=f.next.next
            else:
                f=f.next
                continue
            if s==f:
                return True
        
        return False
        
