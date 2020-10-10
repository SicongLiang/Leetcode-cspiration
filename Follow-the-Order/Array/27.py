# 27. 移除元素(Easy)
##########################
##########################
My solution:
##########################
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while(1):
            if count == len(nums):
                break
            if nums[count] == val:
                nums.remove(val)
                continue
            count += 1

        return len(nums)
##########################
题解：
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)

因为remove会移除列表中的元素，使得len(nums)变小，使用[:]可以对列表进行复制！！！
* for循环不要一直使用range，直接in list也可以！！
