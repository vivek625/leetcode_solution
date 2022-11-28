class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in matches:
            if i[-1] not in dic:
                dic[i[-1]] = 1
            else:
                dic[i[-1]] += 1
        # print(dic)
        temp =set()
        for i in matches:
            if i[0] not in dic:
                temp.add(i[0])
        # print(temp)
        temp_2 = []
        for i in dic:
            if dic[i] == 1:
                temp_2.append(i)
        # print(temp_2)
        temp = list(temp)
        res = []
        temp.sort()
        temp_2.sort()
        res.append(temp)
        res.append(temp_2)
        return res
