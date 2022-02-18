class Solution:
   def twoSum(self, nums, target):
       tmp = {}
       for i, val in enumerate(nums):
           res = target - nums[i]
           
           if res in tmp:
               return [i, tmp[res]]
            
           tmp[val] = i