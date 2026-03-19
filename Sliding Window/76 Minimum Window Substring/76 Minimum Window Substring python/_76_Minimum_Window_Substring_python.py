from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        need = 0
        for x in t : 
            if count_t[x] == 0 :
                need += 1
            count_t[x] += 1
        have, left, start_min, end_min = 0, 0, 0, 0
        min_len = float('inf')
        for right in range(len(s)) : 
            count_s[s[right]] += 1
            if count_s[s[right]] == count_t[s[right]] : 
                have += 1
            while left < right and count_s[s[left]] > count_t[s[left]] :
                count_s[s[left]] -= 1
                left += 1
            if have == need :
                if (right - left + 1) < min_len:
                    start_min = left
                    end_min = right
                    min_len = right - left + 1
        if (min_len == float('inf')) :
            return ""
        return s[start_min : end_min + 1]
print(Solution().minWindow("ADOBECODEBANC", "ABC"))