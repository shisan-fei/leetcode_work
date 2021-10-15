#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  #建立一个哈希表
        num = 0
        len_s = len(s)
        for i in range(len_s):
            if i<len_s-1 and hash.get(s[i]) < hash.get(s[i+1]):   #当前一位小于后一位时
                # num = num - hash[s[i]]  
                num -= hash[s[i]]          #总和
            else:
                num = num + hash.get(s[i]) 
        return num          
# @lc code=end
test = Solution()
str=test.romanToInt('IV')
print(str)

