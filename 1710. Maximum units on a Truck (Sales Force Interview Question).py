class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
            boxTypes=sorted(boxTypes, key = lambda x:x[1],reverse = True)
            sum=0
            i=0
            while truckSize: 
                if i>=len(boxTypes):
                    break 
                sum=sum+boxTypes[i][1]
                boxTypes[i][0]=boxTypes[i][0]-1
                if boxTypes[i][0] == 0:
                    i = i+1
                truckSize = truckSize - 1     
            return sum 
