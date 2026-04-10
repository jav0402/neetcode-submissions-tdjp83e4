class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashing
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

