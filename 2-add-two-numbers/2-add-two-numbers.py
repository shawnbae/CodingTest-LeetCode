from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1, res2, cnt1, cnt2 = 0, 0, 0, 0
        nxt1, nxt2 = l1, l2
        
        while nxt1:
            res1 += 10**(cnt1)*nxt1.val
            nxt1 = nxt1.next
            cnt1 += 1
    
        while nxt2:
            res2 += 10**(cnt2)*nxt2.val
            nxt2 = nxt2.next
            cnt2 += 1
            
        li = [int(char) for char in str(res1+res2)]
        res = ListNode()
        for i in range(0,len(li)):
            if i == len(li)-1:
                res.val = li[i]
            else:
                temp = ListNode()
                temp.val = li[i]
                temp.next = res.next
                res.next = temp
        return res