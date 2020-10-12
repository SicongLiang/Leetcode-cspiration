# 189. 旋转数组(Medium)
##########################
##########################
# 2. 使用额外的数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_2 = nums[:]
        length = len(nums)
        for i in range(0,length,1):
            nums[i] = nums_2[(i-k)%length]
* 时间复杂度：O(n)
* 空间复杂度: O(n)
##########################
题解：(PS: 使用 temp 不增加空间复杂度)
1. 使用反转（三次）
* 这个方法基于这个事实：当我们旋转数组 k 次， k%n 个尾部元素会被移动到头部，剩下的元素会被向后移动。

在这个方法中，我们首先将所有元素反转。然后反转前 k 个元素，再反转后面 n−k 个元素，就能得到想要的结果。

class Solution:
    def reverse(self, nums:List[int], start, end) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # 有可能 k 大于length！！！
        # 同一个 class 里面的函数，调用要加self
        self.reverse(nums, 0, len(nums) - 1) 
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
* 时间复杂度：O(n)
* 空间复杂度: O(1)
