class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = Counter(target)
        e = Counter(arr)
        ee = d-e
        return False if ee else True
