class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array to find adjacent pairs with minimum difference
        arr.sort()
      
        # Find the minimum absolute difference between consecutive elements
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_diff = min(min_diff, diff)
      
        # Collect all pairs that have the minimum absolute difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
      
        return result