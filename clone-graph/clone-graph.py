"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph = {}
        print(node)
        if(node == None):
            return None
        def dfs(node):
            if(node != None and node.val in graph):
                return graph[node.val]
            newNode = Node(node.val)
            graph[node.val] = newNode
            newChildren = []
            print(node.val)
            for child in node.neighbors:
                # if(child.val not in graph):
                newChild = dfs(child)
                newChildren.append(newChild)
            newNode.neighbors = newChildren
            graph[node.val] = newNode
            return newNode
        return dfs(node)