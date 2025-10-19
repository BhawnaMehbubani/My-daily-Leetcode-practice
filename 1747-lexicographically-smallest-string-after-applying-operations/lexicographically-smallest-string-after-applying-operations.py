class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # Initialize BFS queue with the original string
        queue = deque([s])
      
        # Keep track of visited strings to avoid cycles
        visited: Set[str] = {s}
      
        # Initialize result with the original string
        smallest_string = s
      
        # BFS to explore all possible string transformations
        while queue:
            current_string = queue.popleft()
          
            # Update the smallest string if current is lexicographically smaller
            if smallest_string > current_string:
                smallest_string = current_string
          
            # Operation 1: Add 'a' to all odd-indexed digits (modulo 10)
            transformed_add = ''.join(
                str((int(char) + a) % 10) if index % 2 == 1 else char 
                for index, char in enumerate(current_string)
            )
          
            # Operation 2: Rotate string by 'b' positions to the right
            # Take last b characters and move them to the front
            transformed_rotate = current_string[-b:] + current_string[:-b]
          
            # Add both transformations to queue if not visited
            for transformed in (transformed_add, transformed_rotate):
                if transformed not in visited:
                    visited.add(transformed)
                    queue.append(transformed)
      
        return smallest_string