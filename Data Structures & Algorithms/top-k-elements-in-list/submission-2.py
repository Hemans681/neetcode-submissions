class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = freq_dict[num]+1
            else:
                freq_dict[num] = 1

        # print(freq_dict)
        # freq_values = sorted(freq_dict.values(), reverse=True)
        sorted_dict_list = sorted(freq_dict.items(), key=lambda item:item[1], reverse = True)
        # print(sorted_dict_list)
        top_k_list = []
        for item in sorted_dict_list[:k]:
            top_k_list.append(item[0])
        # sorted_dict_list = []
        # sorted_dict_list = [key for item in freq_values[:k]  for key,value in freq_dict.items() if freq_dict[key] = item] 
        # for val in freq_values[:k]:
        #     for key, value in freq_dict.items():
        #         # Sahi comparison (==) aur check ki key pehle se list me na ho
        #         if value == val and key not in sorted_dict_list:
        #             sorted_dict_list.append(key)

        return top_k_list