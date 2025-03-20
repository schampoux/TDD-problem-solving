# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# test case 1: The list has a cycle in it 
# test case 2: The list does not have a cycle in it 
# test case 3: The input list is empty
# test case 4: The input list contains null
# test case 5: The input is of the wrong type 

import unittest
from typing import Optional
from xmlrunner import XMLTestRunner
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return True

class TestHasCycle(unittest.TestCase):
    def create_linked_list(self, values, pos):
        if not values: 
            return None 
        
        nodes = [ListNode(val) for val in values]
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        if pos != -1:
            nodes[-1].next = nodes[pos]

        return nodes[0]

    def test_create_linked_list_valid(self):
        head = self.create_linked_list(values = [3,2,0,-4], pos = 1)
        self.assertIsInstance(head, ListNode)

    def test_create_linked_list_invalid(self):
        head = self.create_linked_list(values = [3,2,0,-4], pos = -1)
        # The .next of the last node should point to None. 
        self.assertIsNone(head.next.next.next.next)
        
    # write a failing test 
    def test_cycle_detected(self):
        # we need a cyclic list 
        # This list will cycle from the last node to the third 

        cyclic_linked_list = self.create_linked_list(values=[3,4,0,-4], pos=2)
        solution = Solution()
        self.assertTrue(solution.hasCycle(head = cyclic_linked_list))


    def test_no_cycle_detected(self):
        cyclic_linked_list = self.create_linked_list(values=[3,4,0,-4], pos=-1)
        solution = Solution()
        self.assertFalse(solution.hasCycle(head = cyclic_linked_list))

if __name__ == '__main__':
    unittest.main(warnings='ignore', testRunner=XMLTestRunner(output='test-reports'))
