import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word.lower() for word in re.sub(r"[!?',;.]", " ",paragraph).split() if word not in banned]
        return sorted(Counter(words).items(), key=lambda x: (-x[1],x[0]))[0][0]