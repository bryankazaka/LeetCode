class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        iLen = len(strs)
        counter = 0
        output = ""
        index = 0
        testTemp = ""
        imax = 0
        for x in strs:
            if len(x)> imax:
                imax = len(x)
        while(index<imax):
            if counter == iLen:
                counter = counter%iLen
                index+=1
                output = output + testTemp
                testTemp = ""
            try: 
                if counter == 0:
                    testTemp = (strs[counter])[index:index+1]
                else:
                    if testTemp != (strs[counter])[index:index+1]:
                        return output
            except:
                return output
            counter+=1
        return output
            
