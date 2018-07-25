import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        neg = False
        

        # Filter negative number
        if(x[0] == '-'):
            neg = True
            x = x[1:len(x)]

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

        # Remove leading zeros
        ret_arr = str(int(''.join(ret_arr))) 

        # Check signed integer   
        if(neg):
            ret_arr = '-' + ret_arr
        
        # Check for overflow integer
        ret_arr = int(ret_arr)
        if(ret_arr < (-2 ** 31) or ret_arr > (2 ** 31) - 1 ):
            return 0
        
        return ret_arr
    
### Test case ###

# x = -8463847412 # Test case 1: Under the 32-bit signed integer (negative)
# x = -9463847412 # Test case 2: Overflow negative by 1
# x = 7463847412 # Test case 3: Under the 32-bit signed integer (positive)
# x = 8463847412 # Test case 4: Overflow positive by 1
x = 123456

out = Solution()
print(out.reverse(x))