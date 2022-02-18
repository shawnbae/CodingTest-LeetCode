class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, res = 0, len(height)-1, 0
        left_max, right_max = height[left], height[right]
        
        while left <= right:
            # 각 방향에서의 maximum을 먼저 업데이트
            if left_max < height[left]:
                left_max = height[left]
            if right_max < height[right]:
                right_max = height[right]
            
            # 양 Pointer의 maximum값에 따라 left, right를 조정
            if left_max == right_max:
                if left == right:
                    res += left_max - height[left]
                    left += 1
                else:
                    res += left_max - height[left]
                    res += right_max - height[right]
                    left += 1
                    right -= 1
            
            elif left_max < right_max:
                res += left_max - height[left]
                left += 1
            
            elif right_max < left_max:
                res += right_max - height[right]
                right -= 1
                
        return res