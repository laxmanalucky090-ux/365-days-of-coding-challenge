class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        for i in range(n):
            # odd length palindrome
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

            # even length palindrome
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

        return longest