from typing import List 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        self.nums = nums 
        self.length = len(nums) 

        for i in range(0, len(nums)+1):
            if i in nums: 
                continue 
            else:
                self.missing = i
            return self.missing 
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        vector = [-1] * (n+1)
        for num in nums:
            vector[num] = num 
        for i in range(len(vector)):
            if vector[i] == -1:
                return i
        return 0

if __name__ == "__main__":
    nums = [3, 0, 1]
    inst = Solution()
    print(inst.missingNumber(nums=nums))

    inst2 = Solution2()
    print(inst2.missingNumber(nums = nums))