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
        # preorder traversal
        if(root == None):
            return "#,"
        serialized = str(root.val) + ","
        serialized += self.serialize(root.left)
        serialized += self.serialize(root.right)
        return serialized
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            if(( data[0] == "#")):
                data.pop(0)
                return None
            node = TreeNode(int(data[0]))
            data.pop(0)
            node.left = helper(data)
            node.right = helper(data)
            return node
        data = data.split(',')
        node = helper(data)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))