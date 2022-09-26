# 135 candy
def candy(self, ratings: list[int]) -> int:
    candies = [1] * len(ratings)
#     print(candies)
    def compare_to_previous_child():
        for child in range(1, len(ratings)):
            prev_child = child - 1
            if ratings[child] > ratings[prev_child]:
                candies[child] = max(candies[child], candies[prev_child] + 1)
                
    compare_to_previous_child()
    candies = [*reversed(candies)]
#     print(candies)
    ratings = [*reversed(ratings)]
#     print(ratings)
    compare_to_previous_child()
#     print(candies)
    return sum(candies)
