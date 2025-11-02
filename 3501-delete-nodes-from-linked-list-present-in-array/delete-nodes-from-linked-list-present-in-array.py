# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        # Convert nums to a set for O(1) lookups
        nums_set = set(nums)
        
        # Create a dummy node to handle edge cases more easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Iterate through the linked list
        while current.next:
            if current.next.val in nums_set:
                # Skip the node with value in nums
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return dummy.next

# Example usage:
def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Create linked list for the example: [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.modifiedList([1, 2, 3], head)
print_list(new_head)  # Output: 4 -> 5
