class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            char_arr = [0] * 26

            for letter in word:
                char_arr[ord(letter) - ord('a')] += 1
            
            group[tuple(char_arr)].append(word)
        
        res = []

        for val in group.values():
            res.append(val)
        
        return res
        
