class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}  # sorted: unsorted str

        for s in strs:
            # sort first then add count
            sorted_str = "".join(sorted(s))

            if sorted_str not in str_map:
                # initialize it first
                str_map[sorted_str] = []
            str_map[sorted_str].append(s)
        # expecting a list
        return list(str_map.values())
