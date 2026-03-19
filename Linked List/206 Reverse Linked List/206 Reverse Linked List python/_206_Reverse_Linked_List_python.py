from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
head.next= node1
node1.next = node2
node2.next = node3
print(Solution().reverseList(head).val)
