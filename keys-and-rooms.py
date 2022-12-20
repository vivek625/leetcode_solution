class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack =[]
        stack = stack+rooms[0]
        l = len(rooms)
        visit = set()
        visit.add(0)
        while stack:
            if l == len(visit):
                return True
            curr = stack.pop(0)
            if curr not in visit:
                visit.add(curr)
                stack = stack+rooms[curr]
        if len(visit) == l:
            return True
        else:
            return False
