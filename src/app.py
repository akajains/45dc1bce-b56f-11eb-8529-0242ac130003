class  LongestIncreasingSequence():
    def Find(self):
        input=' 6 5 5 6 7 4 5'
        #map input to python array
        inputList = list(map(int,input.split()))
        #member variable declaration        
        tempResult=[]
        candidateSeq={}
        for k in range(len(inputList)):
            
            if k and inputList[k-1] >= inputList[k]:                
                flag = k                
                tempResult.clear()
                tempResult.append(inputList[k])
                
                if not len(tempResult) in candidateSeq:
                    candidateSeq[len(tempResult)] = tempResult.copy()
                
            else:                
                tempResult.append(inputList[k])                
                if not len(tempResult) in candidateSeq:
                    candidateSeq[len(tempResult)] = tempResult.copy()

        # map array into the desired output separated by single whitespace
        longestSequence = candidateSeq[max(candidateSeq)]
        
        #print(longestSequence)
        
        return longestSequence
        
longestIncreatingSequence = LongestIncreasingSequence()

print(longestIncreatingSequence.Find())

