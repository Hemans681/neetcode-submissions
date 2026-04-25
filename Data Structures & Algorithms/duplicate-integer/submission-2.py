class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        seek = set()
        for num in nums:
            if num in seek:
                return True
            else:
                # add number is seen first time
                seek.add(num)
            # freq[num] =1 if num not in freq

        return False

