# Problem Number : 2
# Solved on : 4 October 2024

# DESCRIPTION
""" 
  Given a string s, find the length of the longest substring without repeating characters.
  
Example 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.
"""

#SOLUTION :
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        tries = 0
        teststring = []
        finalstring = []

        while tries < len(s):
            pointer = tries
            while pointer < len(s):
                if s[pointer] in teststring:
                    finalstring.append(teststring)
                    teststring = []
                    break
                else:
                    teststring.append(s[pointer])
                    if len(s) == 1:
                        finalstring.append(s)
                        break
                pointer += 1

            tries += 1
        len1 = 0
        for x in finalstring:
            t = len(x)
            if t > len1:
                len1 = t
        return len1
