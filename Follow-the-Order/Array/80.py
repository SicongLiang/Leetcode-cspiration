# 80. 删除排序数组中的重复项 II(Medium)
##########################
##########################
参考26的双指针写报错，参考27的remove使用 for in range 报错out of list
##########################
题解：
1. 使用remove
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 1
        count = 1
        # for i in range(1, len(nums)):
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count = count + 1
                if count > 2:
                    nums.remove(nums[i])
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)
     
使用 for i in range 会报错 out of list！而while不会！
* 因为for i in range的loop里，无法对 i 做任何操作！！！！！！！！！

*** （难想到）
2. 覆盖多余的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        j, count = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
########################################### 以上均没问题，写得出
            # 若 count <=2，则我们将 i 所指向的元素移动到 j 位置，并同时增加 i 和 j。这样双指针！不需要remove！最后返回j即可
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j


