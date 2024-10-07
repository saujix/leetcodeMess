# Problem Number : 5
# Solved on : 7 October 2024

# DESCRIPTION
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:
        final = 0
        if x > ((2**31)-1):
            return final
        else :
            i = 1
            final = ""
            if x < 0:
                x = -x
                x = str(x)
                while i <= (len(x) ):
                    final += x[-i]
                    i += 1
                final = int(final)
                if final > ((2**31)-1):
                    return 0
                else :
                    final = -final
                    return(final)
            else:
                x = str(x)
                while i <= (len(x) ):
                    final += x[-i]
                    i += 1
                final = int(final)
                if final > ((2**31)-1):
                    return 0
                else :
                    return(final)
