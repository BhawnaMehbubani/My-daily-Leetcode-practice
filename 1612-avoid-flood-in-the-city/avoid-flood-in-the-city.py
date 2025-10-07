class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        # Initialize result array with -1 (default for rainy days)
        result = [-1] * n
      
        # Keep track of sunny days (when we can dry a lake)
        sunny_days = SortedList()
      
        # Dictionary to store the last day each lake was filled
        # Key: lake number, Value: day index when it rained on this lake
        last_rain_day = {}
      
        for day, lake in enumerate(rains):
            if lake > 0:  # Rainy day (lake > 0 means it rains on this lake)
                # Check if this lake was already full
                if lake in last_rain_day:
                    # Find the first sunny day after the last rain on this lake
                    # We need to dry this lake before it rains again
                    sunny_day_idx = sunny_days.bisect_right(last_rain_day[lake])
                  
                    # If no sunny day available after last rain, flood is inevitable
                    if sunny_day_idx == len(sunny_days):
                        return []
                  
                    # Use this sunny day to dry the current lake
                    dry_day = sunny_days[sunny_day_idx]
                    result[dry_day] = lake
                  
                    # Remove the used sunny day from available days
                    sunny_days.discard(dry_day)
              
                # Update the last rain day for this lake
                last_rain_day[lake] = day
            else:  # Sunny day (lake == 0)
                # Add this day to available sunny days
                sunny_days.add(day)
                # Default: dry lake 1 (can be any valid lake number)
                result[day] = 1
      
        return result