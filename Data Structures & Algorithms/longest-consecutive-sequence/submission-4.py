class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        n=len(sorted_nums)
        longest_subsequence= set()
        lengths = []
        for i in range(n):
            longest_subsequence.add(sorted_nums[i])
            if i+1<n:
                if sorted_nums[i+1]-sorted_nums[i]==1 or sorted_nums[i+1]==sorted_nums[i]:
                    continue
            
                lengths.append(len(longest_subsequence))
                longest_subsequence.clear()
                continue

            lengths.append(len(longest_subsequence))
            
        return max(lengths)

            