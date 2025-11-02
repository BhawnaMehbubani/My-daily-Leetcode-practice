class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # Initialize grid: 0 = unguarded, 1 = guarded, 2 = guard/wall
        grid = [[0] * n for _ in range(m)]
      
        # Mark guards on the grid
        for row, col in guards:
            grid[row][col] = 2
      
        # Mark walls on the grid
        for row, col in walls:
            grid[row][col] = 2
      
        # Direction vectors: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        # For each guard, mark all cells they can see in four directions
        for guard_row, guard_col in guards:
            for delta_row, delta_col in directions:
                current_row, current_col = guard_row, guard_col
              
                # Continue in current direction until hitting boundary or obstacle
                while (0 <= current_row + delta_row < m and 
                       0 <= current_col + delta_col < n and 
                       grid[current_row + delta_row][current_col + delta_col] < 2):
                    current_row += delta_row
                    current_col += delta_col
                    grid[current_row][current_col] = 1  # Mark as guarded
      
        # Count unguarded cells (cells with value 0)
        unguarded_count = sum(cell == 0 for row in grid for cell in row)
      
        return unguarded_count
