class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Remove minimum cost balloons to ensure no two adjacent balloons have the same color.
      
        Args:
            colors: String representing colors of balloons
            neededTime: List of integers representing time needed to remove each balloon
      
        Returns:
            Minimum total time to remove balloons
        """
        total_cost = 0
        current_index = 0
        n = len(colors)
      
        # Process groups of consecutive balloons with the same color
        while current_index < n:
            # Start of a new group
            group_start = current_index
            group_sum = 0
            max_time = 0
          
            # Find all consecutive balloons with the same color
            while current_index < n and colors[current_index] == colors[group_start]:
                # Add current balloon's removal time to group sum
                group_sum += neededTime[current_index]
                # Track the maximum removal time in this group
                if max_time < neededTime[current_index]:
                    max_time = neededTime[current_index]
                current_index += 1
          
            # If group has more than one balloon, we need to remove all except one
            # Keep the balloon with maximum removal time (most expensive to remove)
            # Remove all others (cheaper ones)
            if current_index - group_start > 1:
                total_cost += group_sum - max_time
      
        return total_cost
