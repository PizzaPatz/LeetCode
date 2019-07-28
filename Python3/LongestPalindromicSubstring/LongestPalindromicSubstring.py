class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(s == '' or len(s) < 0):
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            left_palindrome = self.expanding_center(s, i, i)
            right_palindrome = self.expanding_center(s, i, i+1)
            sub_highest_palindrome_num = max(left_palindrome, right_palindrome)
            if(sub_highest_palindrome_num > end - start):
                start = int(i - (sub_highest_palindrome_num - 2) / 2)
                end = int(i + sub_highest_palindrome_num /2)
        return s[start:end+1]
        
    def expanding_center(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
        
out = Solution()
print(out.longestPalindrome("babad"))
print(out.longestPalindrome("cbbd"))

