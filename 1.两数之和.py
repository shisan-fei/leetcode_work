#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    #在函数传参中指定数据类型要typing模块
        hash={}     #创建一个字典用来存放列表中数字和数字所在索引
        j=-1        #j用来返回数字所在索引
        for ind,num in enumerate(nums):   #enumerate返回可迭代对象的值和索引('索引'，'值')
            hash[num] = ind               #字典的键为列表的数字，值为数字的索引
        # print(hash)           
        for ind,num in enumerate(nums):   
            j=hash.get(target-num)        #target-num就是和减去列表中任意一个数字，结果在字典中找，找到后将索引返回给j
            if j != None and  ind !=j:    #target-num的结果找不到j就会返回none
                return [ind,j]
            
# @lc code=end
nums = [2,5,3,7,9]
test = Solution()
num =test.twoSum(nums,8)
print(num)

