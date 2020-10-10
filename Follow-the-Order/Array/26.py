# 26. 删除排序数组中的重复项(Easy)
##########################
##########################
My solution: 执行用时：668 ms, 在所有 Python3 提交中击败了 9.71% 的用户，时间复杂度太高
##########################
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            count = nums[0]
            for i, val in enumerate (nums[:]):
                if i == 0:
                    continue
                if val == count:
                    nums.remove(val)
                else:
                    count = val 
            return len(nums)
            
##########################
题解：双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i  = 0
        for j in range(1, len(nums)): # 快指针 j 得从 i+1 即 1 开始！
            if nums[j] != nums[i]: 
                i += 1
                nums[i] = nums[j]
        
        return i + 1
     
数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。只要 nums[i] = nums[j]，我们就增加 j 以跳过重复项。
当我们遇到 nums[j] \neq nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复制到 nums[i + 1]。然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。
* 题目中提到：“你不需要考虑数组中超出新长度后面的元素。”！！！！ 所以只要修改前面的元素使得数组没有重复的元素，然后返回一个 i+1的长度即可！


