class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        
        shortest_element_len = 201
        shortest_elelement = ""
        for shortest in strs:
            if len(shortest) < shortest_element_len:
                shortest_element_len = len(shortest)
                shortest_elelement = shortest
        
        longest_common_prefix = []
        for x in range(shortest_element_len):
            if x + 1 <= shortest_element_len:
                longest_common_prefix.append(shortest_elelement[x])
                for y in strs:
                        if y[0:x+1] not in "".join(longest_common_prefix) and len(longest_common_prefix) > 0:
                            longest_common_prefix.pop()
                            return "".join(longest_common_prefix)
        
        return "".join(longest_common_prefix)