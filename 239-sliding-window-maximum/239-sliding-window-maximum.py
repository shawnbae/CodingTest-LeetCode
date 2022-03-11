class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        res = []
        for i, cur in enumerate(nums[:k-1]):
            while q and nums[q[-1]]<cur: q.pop()
            q.append(i) # Store index 
        
        for i in range(k-1,len(nums)):
            cur=nums[i]
            # Pop elements from tail if tail elements are smaller than cur
            while q and nums[q[-1]]<cur: q.pop()
            q.append(i)
            
            res.append(nums[q[0]]) # Max stored at Head
            
            # Since queue is in sorted index low->high
            # If head is == indToRemove(rem) part then popleft
            rem=i-k+1
            if q[0]==rem:  q.popleft()
            
        return res