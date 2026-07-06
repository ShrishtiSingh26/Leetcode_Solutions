class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        v=0
        for i in range(len(s)-1):
            if dict1[s[i]]>=dict1[s[i+1]]:
                v=v+dict1[s[i]]
            elif dict1[s[i]]<dict1[s[i+1]]:
                v=v-dict1[s[i]]
        v=v+dict1[s[-1]]
        return v