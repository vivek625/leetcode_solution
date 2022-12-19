class Solution:

    def __init__(self, nums: List[int]):
        self.num1 = nums
        self.shuffle1 = [num for num in nums]

        

    def reset(self) -> List[int]:
        return self.num1
        

    def shuffle(self) -> List[int]:
        shuffle(self.shuffle1)
        return self.shuffle1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
