# Problem Number : 3
# Solved on : 5 October 2024

# DESCRIPTION
"""
Given a string s, return the longest palindromic substring in s.

The overall run time complexity should be O(log (m+n)).

lets just move on with life without the upper line

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(inpStr):
            pointer = 0
            midlen = (len(inpStr)//2)
            while pointer <= midlen:
                if inpStr[pointer] == inpStr[-((pointer)+1)]:
                    if pointer == midlen:
                        return True
                else:
                    return False
                pointer +=1

        finalList = []
        
        if isPalindrome(s):
            return s
        else:
            base = 0
            while base < len(s):
                finalList.append(s[base])

                pointer = base + 1
                string = f"{s[base]}"
                while pointer < len(s):
                    string += s[pointer]
                    if isPalindrome(string):
                        finalList.append(string)
                    pointer += 1
                base +=1

        bigWord = max(finalList, key=len)
        return bigWord

