from queue import PriorityQueue
class TimeMap:

    def __init__(self):
        self._vault = defaultdict(PriorityQueue)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._vault[key].put((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self._vault[key].empty():
            return ''

        time, value = None, ''
        print(self._vault[key].queue[0])
        while not self._vault[key].empty() and self._vault[key].queue[0][0] <= timestamp:
            time, value = self._vault[key].get()
        if time and value:
            self._vault[key].put((time, value))
        return value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
