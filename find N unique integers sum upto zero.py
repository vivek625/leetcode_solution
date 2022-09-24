 class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]

        width = int(n / 2)

        result = list(range(-1 * width, width + 1))

        if not n % 2:
            return [*result[:width], *result[width + 1:]]

        return result
