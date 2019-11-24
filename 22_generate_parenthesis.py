import argparse
class Solution:
    def generateParenthesis(self, n): 
        queue = []
        queue.append(('(',n-1 ,n))
        result = []
        while queue:
            string, d_o, d_c = queue.pop()
            
            if d_o > d_c or d_o < 0:
                continue
                
            if len(string) == 2*n:
                result.append(string)
                continue
                
            queue.append((string+')', d_o, d_c - 1))
            queue.append((string+'(', d_o - 1, d_c))
            
        return result

s = Solution()
parser = argparse.ArgumentParser()
parser.add_argument('-n' , dest = "n", required = True, type=int, help ="number of parenthesis pair")
options = parser.parse_args()

print(s.generateParenthesis(options.n))
