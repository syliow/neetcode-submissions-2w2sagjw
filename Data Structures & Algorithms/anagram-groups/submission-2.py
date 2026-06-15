class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = defaultdict(list)
        for s in strs:
            sortedstr = "".join(sorted(s))
            strmap[sortedstr].append(s)

        return list(strmap.values())
