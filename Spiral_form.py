#  Given an m x n matrix, return all elements of the matrix in spiral order.


# Sample Input/Ouput

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Solutions :

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom = 0,len(matrix)-1
        left,right = 0, len(matrix[0])-1
        
        lst=[]
        direction = 0 
        
        while left<=right and top<=bottom:
            
            if direction == 0:
                
                for i in range(left,right+1):
                    lst.append(matrix[top][i])
                top+=1 
                
            elif direction == 1:
                
                for i in range(top,bottom+1):
                    lst.append(matrix[i][right])
                right-=1 
                
            elif direction == 2:
                
                for i in range(right,left-1,-1):
                    lst.append(matrix[bottom][i])
                bottom-=1 
            
            elif direction == 3:
                
                for i in range(bottom,top-1,-1):
                    lst.append(matrix[i][left])
                left+=1
            
            direction = (direction+1)%4
            
        return lst


# Optimal code :


def spiralOrder(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr= (list(zip(*arr)))[::-1]
    return ans
