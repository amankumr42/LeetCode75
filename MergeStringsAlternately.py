class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        minLen = None
        final_array = []
        if (len(word1) < len(word2)):
            minLen = len(word1)
        else:
            minLen = len(word2)
        for i in range(0, minLen):
            final_array.append(word1[i])
            final_array.append(word2[i])       
        if (minLen < len(word1)):
            final_array.append(word1[minLen: len(word1)])
        elif (minLen < len(word2)):
            final_array.append(word2[minLen: len(word2)]) 
        else:
            pass       
        listToStr = ' '.join([str(elem) for elem in final_array])
        print(listToStr)   
        return  listToStr.replace(" ","") 