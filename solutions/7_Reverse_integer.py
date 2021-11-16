# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        s = list(str(x))
        negative = s[0]== '-'
        if negative:
            s = s[1:]
        sr = ''.join(list(reversed(s)))
        first_char = sr[0]
        while first_char == '0':
            sr = sr[1:]
            first_char = sr[0]
        if negative:
            sr = '-' + sr
        res = eval(sr)
        return res if -pow(2,31)<=res<=pow(2,31)-1 else 0