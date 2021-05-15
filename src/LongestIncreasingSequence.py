import sys
class  LongestIncreasingSequence():
    
    def __init__(self): self.candidateSeq={}; self.tempResult=[]    
    
    def Find(self, args):        
        #map input to python array
        inputList = list(map(int,args.split()))
        #member variable declaration        
        #tempResult=[]        
        for k in range(len(inputList)):            
            if k and inputList[k-1] >= inputList[k]:                
                flag = k                
                self.tempResult.clear()
                self.tempResult.append(inputList[k])                
                self.AddtoCollection(len(self.tempResult))                
            else:                
                self.tempResult.append(inputList[k])                
                self.AddtoCollection(len(self.tempResult))

        # map array into the desired output separated by single whitespace
        longestSequence =  " ".join(map(str,self.candidateSeq[max(self.candidateSeq)]))
        return longestSequence
    
    def AddtoCollection(self,key):
        if not key in self.candidateSeq:
            self.candidateSeq[key] = self.tempResult.copy()
        
if __name__ == '__main__':        
    longestIncreatingSequence = LongestIncreasingSequence()
    print(longestIncreatingSequence.Find(sys.argv[1]))
