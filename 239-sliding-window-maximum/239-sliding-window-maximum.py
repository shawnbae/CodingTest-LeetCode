class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        res = []
        for i, cur in enumerate(nums[:k-1]):
            while q and nums[q[-1]]<cur: q.pop()
            q.append(i)
        
        for i in range(k-1,len(nums)):
            cur=nums[i]
            
            while q and nums[q[-1]]<cur: q.pop()
            q.append(i)
            
            res.append(nums[q[0]])
            rem=i-k+1
            if q[0]==rem:  q.popleft()
            
        return res