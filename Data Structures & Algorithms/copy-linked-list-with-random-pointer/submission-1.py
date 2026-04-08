"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}

        itr = head
        previousNode = None
        flag = True
        newHead = None
        while itr:
            currentNode = Node(itr.val)
            nodeMap[itr] = currentNode
            if flag:
                newHead = currentNode
                flag = False
            if previousNode:
                previousNode.next = currentNode
            itr = itr.next
            previousNode = currentNode

        itr = head
        itr2 = newHead
        

        while itr:
            if itr.random != None:
                itr2.random = nodeMap[itr.random]
            itr = itr.next
            itr2 = itr2.next
            

        return newHead    

