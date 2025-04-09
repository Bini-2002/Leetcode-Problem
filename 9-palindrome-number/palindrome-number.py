class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        reversed_y = y[::-1]

        if str(x) == reversed_y:
            return True
        else:
            return False
