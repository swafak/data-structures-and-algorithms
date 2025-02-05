# Using Inbuilt Methods – O(n) Time and O(1) Space
def arrayReverse(nums):
    
    nums.reverse()

numbers = [35,5,6,799,9,0,4]
arrayReverse(numbers)
print(numbers)


# Using a temporary array – O(n) Time and O(n) Space
def arrReverse(nums):
    n = len(nums)
    temp = [0] * n
    
    for i in range(n):
     
        temp[i] = nums[n-i-1]
    for i in range(n):
        nums[i] = temp[i]
        
    
arrReverse(numbers)
print(numbers)

# Using Two Pointers – O(n) Time and O(1) Space
# optimal solution


def arrsReverse(nums):
    
    n = len(nums)
    left = 0
    right = n - 1
    
    while left < right:
        
        nums[left], nums[right] = nums[right],nums[left]
        
        left +=1
        right -=1
        

arrsReverse(numbers)
print(numbers)
        
        


        
        
