#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            out = [[1],[1,1]]
            for i in range(numRows-2):
                new = []
                try:
                    last = out.pop()
                    last_size = len(last)
                    new.append(1)
                    for j in range(last_size-1):
                        new.append(last[j]+last[j+1])
                    new.append(1)
                    out.append(last)
                    out.append(new)
                except:
                  pass
        return out
