from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        dic = Counter(stones)
        
        for key in dic.keys():
            if key in jewels and dic[key] > 0:
                answer += dic[key]
        
        return answer