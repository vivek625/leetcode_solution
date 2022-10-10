class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = []
        heights_dict = dict(zip(heights,names))
        for height in sorted(heights,reverse = True):
            s.append(heights_dict[height])
        return (s)
