class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for item in range(len(s)):
            print(s[item])
            dict1[s[item]]= dict1.get(s[item], 0)+1
            dict2[t[item]]=dict2.get(t[item],0)+1
            
        return dict1==dict2
