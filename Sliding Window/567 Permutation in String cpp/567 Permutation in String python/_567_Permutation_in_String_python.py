class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26
        for x in s1 :
            count1[ord(x) - ord('a')] += 1
        left = 0
        for right in range(len(s2)) :
            count2[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 == len(s1) :
                if count1 == count2 :
                    return True
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1
        return False
print(Solution().checkInclusion("abc", "lecabee"))