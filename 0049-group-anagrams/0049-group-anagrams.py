import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            mp[key].append(s)

        return list(mp.values())