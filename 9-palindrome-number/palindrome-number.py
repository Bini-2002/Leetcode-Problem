class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        original = x
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        if original == reversed_num:
            return True
        return False
                