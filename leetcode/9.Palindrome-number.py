class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringX = str(x)
        if stringX == stringX[::-1]:
            return True
        else:
            return False
