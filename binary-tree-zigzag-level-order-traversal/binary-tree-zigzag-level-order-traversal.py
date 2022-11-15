# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        queue = [(root, 0)]
        prev = 0
        temp = []
        final = []
        while(len(queue) > 0):
            top = queue[0]
            queue = queue[1:len(queue)]
            if(top[1]!= prev):
                if(prev% 2 == 1):
                    temp = temp[::-1]
                    final.append(temp)
                else:
                    final.append(temp)
                prev = top[1]
                temp = [top[0].val]
            else:
                temp.append(top[0].val)
            if(top[0].left != None):
                queue.append((top[0].left, top[1]+1))
            if(top[0].right != None):
                queue.append((top[0].right, top[1]+1))
                
        if(len(temp)>0):
            if(prev% 2 == 1):
                temp = temp[::-1]
                final.append(temp)
            else:
                final.append(temp)
        return final
            
        
        