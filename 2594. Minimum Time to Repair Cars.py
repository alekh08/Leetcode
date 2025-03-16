class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = 10**14  
        while left < right:
            mid = (left + right) // 2
            total_cars_possible = sum(int((mid // rank) ** 0.5) for rank in ranks)
            if total_cars_possible >= cars:
                right = mid
            else:
                left = mid + 1
        
        return left
