from typing import List 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # compare num to every other index 
        set_nums = set(nums) 
        if len(set_nums) == len(nums):
            return False
        else: 
            return True 

if __name__ == "__main__":
    nums = [2,3,1,1]
    sol_inst = Solution()
    result = sol_inst.containsDuplicate(nums= nums)
    print(result)