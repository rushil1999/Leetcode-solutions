# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # level order traversal
        serialized = ""
        queue = [root]
        while(len(queue) > 0):
            front = queue[0]
            queue.pop(0)
            if(front == None):
                serialized += "#,"
                continue
            serialized += str(front.val)+","
            queue.append(front.left)
            queue.append(front.right)
            
        return serialized
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if(len(data) == 0):
            return None
        if(data[0]== "#"):
            return None
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while(len(queue) > 0 and i < len(data)):
            node = queue[0]
            queue = queue[1:len(queue)]
            if(data[i] != "#"):
                leftNode = TreeNode(int(data[i]))
                node.left = leftNode
                queue.append(leftNode)
            else:
                node.left = None
            i+= 1
            if(data[i] != "#"):
                rightNode = TreeNode(int(data[i]))
                node.right = rightNode
                queue.append(rightNode)
            else:
                node.right = None
            i+= 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))