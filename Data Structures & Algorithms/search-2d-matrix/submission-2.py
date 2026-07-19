class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for a in range(len(matrix)):
            l,r = 0 , len(matrix[a]) - 1
            while l <= r:  
                mid = l + (r - l) // 2  

                if matrix[a][mid] < target:
                    l = mid + 1  
                elif matrix[a][mid] > target:
                    r = mid - 1  
                else:
                    return True  
                
        return False  








#O(n2)
#        for i in range(len(matrix)):
#            for j in range(len(matrix[0])):
#                if matrix[i][j] == target:
#                    return True 
#        else:
#            return False
        