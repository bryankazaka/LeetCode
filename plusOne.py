class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idigits =""
        for x in digits:
            idigits += str(x)
        idigits = int(idigits)
        idigits+=1
        idigits = str(idigits)
        out = []
        for x in idigits:
            out.append(int(x))
        return out
