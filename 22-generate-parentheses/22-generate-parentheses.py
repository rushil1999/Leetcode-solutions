class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = [('', 0, 0)]
        while(queue):
            s, n_open, n_closed = queue[0]
            print(s)
            queue = queue[1:len(queue)]
            
            if n_open == n_closed == n:
                res.append(s)
                print("Appending", s)
                continue
                
            # add to queue if not satisfactory yet
            if n_open < n:
                queue.append((s + '(', n_open+1, n_closed))
            if n_closed < n_open:
                queue.append((s + ')', n_open, n_closed+1))
        return res