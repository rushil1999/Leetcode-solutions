from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0, 0)]
        nodeList = []
        while(len(stack) > 0):
            top = stack[-1]
            nodeList.append((top[2], top[1], top[0].val))
            # if(top[1] in m):
            #     m[top[1]].append(top[0].val)
            # else:
            #     m[top[1]]= [top[0].val]
            stack = stack[0:len(stack)-1]
            
            if(top[0].left != None):
                stack.append((top[0].left, top[1]+ 1 ,top[2]-1))
            if(top[0].right != None):
                stack.append((top[0].right, top[1]+1, top[2]+1))
            # print(stack)
        nodeList.sort()
        ret = []
        curr_column_index = nodeList[0][0]
        curr_column = []
        for column, row, value in nodeList:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret