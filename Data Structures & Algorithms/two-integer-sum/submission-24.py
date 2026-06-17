class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, x1 in enumerate(nums):
            x2 = target - x1

            if x2 in seen:
                return [seen[x2], i]
            
            seen[x1] = i