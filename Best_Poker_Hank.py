class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        s = []
        k = []
        for i in range(len(ranks)):
            kk = ranks.count(ranks[i])
            sus = suits.count(suits[i])
            s.append(kk)
            k.append(sus)
        ss = max(s)
        kkk = max(k)
        if kkk > 4:
            return("Flush")
        elif ss >= 3:
            return("Three of a Kind")
        elif ss > 1:
            return("Pair")
        else:
            return ("High Card")
