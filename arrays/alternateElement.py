# Given an array arr[], the task is to print every alternate element of the array starting from the first element.

def alternateElement(nums):
    
    output = []
    
    for i in range(0,len(nums), 2):
        output.append(nums[i])
        
    return output

arr = [10, 20, 30, 40, 50]
print(alternateElement(arr))
 
 
        
        