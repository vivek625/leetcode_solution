class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction_sorted = sorted(satisfaction , reverse=True)
        cumulative_dishes_sum = 0
        dishes_sum = 0
        max_dishes_sum = 0
        for dish_satisfaction in satisfaction_sorted:
        #     print(dish_satisfaction)
            cumulative_dishes_sum += dish_satisfaction
            dishes_sum += cumulative_dishes_sum
            max_dishes_sum = max(max_dishes_sum,dishes_sum)
        return (max_dishes_sum)
