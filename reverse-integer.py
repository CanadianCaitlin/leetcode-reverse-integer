# Link to Leetcode problem: https://leetcode.com/problems/reverse-integer/submissions/
# Difficulty: Easy

class Solution:
    def reverse(self, x: int) -> int:
        output = []
        if abs(x) == x:
            for num in str(x):
                output.insert(0, num)
        else:
            x = abs(x)
            for num in str(x):
                output.insert(0, num)
            output.insert(0, "-")
        output = "".join(output)
        if int(output) > 2**31+1 or int(output) < -2**31-1:
            return 0
        return int(output)