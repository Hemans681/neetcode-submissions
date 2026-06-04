import re
class Solution:
    # I viewed solution first to solve this
    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for string in strs:
            encoded_list.append(f"{len(string)}#{string}")
        return ''.join(encoded_list)
            

    def decode(self, s: str) -> List[str]:
        words= []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            word_len = int(s[i:j])
            start_idx = j+1
            end_idx = start_idx+word_len
            
            word = s[start_idx:end_idx]
            words.append(word)
            i = end_idx
            
        return words



