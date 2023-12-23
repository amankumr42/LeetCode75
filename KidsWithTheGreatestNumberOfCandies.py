class Solution:
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        final_res = []
        for i in  candies:
            curr_sum = i + extraCandies
            for k in candies:
                status="false"
                if curr_sum >= max(candies):
                    status = "true"
                break
            final_res.append(status)
        return final_res
         
    
            
            
            
        