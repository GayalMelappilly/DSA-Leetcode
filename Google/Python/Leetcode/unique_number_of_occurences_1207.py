class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        prev_map = {}
        count_map = {}

        for num in arr:
            if num in prev_map:
                prev_map[num] += 1
            else:
                prev_map[num] = 1

        for count in prev_map:
            if prev_map[count] in count_map:
                return False
            else:
                count_map[prev_map[count]] = count
        return True
        

        