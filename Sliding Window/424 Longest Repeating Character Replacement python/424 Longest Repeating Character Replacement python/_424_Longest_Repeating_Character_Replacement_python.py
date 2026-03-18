from collections import defaultdict
from xml.dom.minidom import CharacterData

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left, max_count, max_dup = 0, 0, 0
        for right in range(len(s)) :
            count[s[right]] += 1
            if count[s[right]] > max_count :
                max_count = count[s[right]]
            dup = right - left + 1
            rep = dup - max_count
            if rep > k :
                count[s[left]] -= 1
                dup -= 1
                left += 1
            if dup > max_dup :
                max_dup = dup
        return max_dup
print(Solution().characterReplacement("AAABABB", 1))
