from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [w for w ,_ in Counter(sorted(words)).most_common(k)]
