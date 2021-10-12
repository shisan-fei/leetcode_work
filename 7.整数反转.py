#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:     #x在正负10之内直接返回
            return x
        srt_x = str(x)       #将数值转换为字符串操作
        if srt_x[0] != '-':
            srt_x = srt_x[::-1]
            x = int(srt_x)
        else:
            srt_x=srt_x[:0:-1]
            x=int(srt_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0
solu=Solution()
print(solu.reverse(-123))
# @lc code=end

