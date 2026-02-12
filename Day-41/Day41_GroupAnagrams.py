class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        boxes = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in boxes:
                boxes[key] = []
            boxes[key].append(word)
        return list(boxes.values())