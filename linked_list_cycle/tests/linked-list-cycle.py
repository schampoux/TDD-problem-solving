# Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# test case 1: Empty input -> False 
# test case 2: Valid input (multiple nodes) (cycle) -> True 
# test case 3: Valid input (multiple nodes) (no cycle) -> False 
# test case 4: One node (no cycle) -> False 
# test case 5: One node (cycle) -> True 
# test case 6: Two nodes (no cycle) -> False 
# test case 7: Two nodes (cycle) -> True 


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
        
        visited_nodes = set()
        current = head 

        while current:
            if current in visited_nodes: 
                return True
            visited_nodes.add(current)
            current = current.next 

        return False             
        
        # if the current node is in the set of visited nodes
            # return true because we have a cycle 
        # if the current node is not in the set of visited nodes 
            # while current makes sure the current node is not none. 
            # add it and move on to the next node 
        

class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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
        
    def test_empty_input(self):
        self.assertFalse(self.solution.hasCycle(head = None)
    
    def test_cycle_detected(self):
        cyclic_linked_list = self.create_linked_list(values=[3,4,0,-4], pos=2)
        self.assertTrue(self.solution.hasCycle(head = cyclic_linked_list))
 
    def test_no_cycle_detected(self):
        valid_non_cyclic_linked_list = self.create_linked_list(values=[3,4,0,-4], pos=-1)
        self.assertFalse(self.solution.hasCycle(head = valid_non_cyclic_linked_list))
    

if __name__ == '__main__':
    unittest.main(warnings='ignore', testRunner=XMLTestRunner(output='test-reports'))
