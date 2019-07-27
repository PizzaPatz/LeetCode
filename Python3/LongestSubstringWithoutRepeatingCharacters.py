class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ""
        b = ""
        for i in range(len(s)):
            if s[i] not in b:
                b += s[i]
            else:
                if len(a) < len(b):
                    a = b
                b = b[b.index(s[i])+1:] + s[i]
              
        return max(len(a), len(b))


out = Solution()
# highest_substring_number = out.lengthOfLongestSubstring('abcabcbb')
# highest_substring_number = out.lengthOfLongestSubstring('bbbbb')
highest_substring_number = out.lengthOfLongestSubstring("pwwkew")
print(highest_substring_number)