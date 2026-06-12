class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for idx, val in enumerate(nums):
            prod = 1
            for idx2, items in enumerate(nums):
                if not idx == idx2:
                    prod *= items

            # prod = int(prod /nums[idx])
            prod = int(prod)
            output.append(prod)
        return output