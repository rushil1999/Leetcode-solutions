/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
    "math"
)

func recurse(node *TreeNode, minVal, maxVal int) bool {
    if node == nil {
        return true
    }
    leftBST := recurse(node.Left, minVal, node.Val)
    rightBST := recurse(node.Right, node.Val, maxVal)
    if node.Val <= minVal || node.Val >= maxVal {
        return false
    }
    
    return leftBST && rightBST
}

func isValidBST(root *TreeNode) bool {
    val := recurse(root, math.MinInt, math.MaxInt)  
    return val
}