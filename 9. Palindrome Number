class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        # Also, if the number ends in 0 and is not 0, it's not a palindrome (e.g., 10, 100)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Check if the first half is equal to the reversed second half
        # For odd-digit numbers, discard the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
