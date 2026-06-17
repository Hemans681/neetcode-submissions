class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n=len(sorted_nums)
        longest_subsequence= set()
        lengths = []
        for i in range(n):
            longest_subsequence.add(sorted_nums[i])
            if i+1<n:
                if not sorted_nums[i+1]-sorted_nums[i]==1 and not sorted_nums[i+1]==sorted_nums[i]:
                    lengths.append(len(longest_subsequence))
                    longest_subsequence.clear()
        lengths.append(len(longest_subsequence))
        print(lengths)
        return max(lengths)

            