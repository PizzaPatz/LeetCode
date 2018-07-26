import math
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        # If negative integer, we can rule out it
        # will not be palindrome
        if(x[0] == '-'):
            return False
        
        ret_arr = [0]*len(x)
        last = len(x) - 1
        ret_arr = [0]*len(x)

        # Swap loop
        for i in range(0, math.ceil(last/2)):
            ret_arr[i] = x[last - i]
            ret_arr[last-i] = x[i]

        # Check even number
        if((len(x) % 2) != 0):
            ret_arr[math.ceil(last/2)] = x[math.ceil(last/2)]
        else:
            pass 

        # Convert array into string
        ret_arr = ''.join(ret_arr)
        
        # Compare the original string and return string
        if(ret_arr == x):
            return True
        return False

x = 10

out = Solution()
print(out.isPalindrome(x))