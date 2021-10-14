#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
from typing import List
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        if str_x == str_x[::-1]:     #将数字反转
            return True
        elif str_x[0] == '-':
            return False
        else:
            return False
# @lc code=end
test = Solution()
print(test.isPalindrome(1111))

