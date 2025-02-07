def isSorted(nums):
    
    n = len(nums)
    
    if (n == 0 or n == 1):
        return 'yes'
            
    for i in range(n-1):
        if nums[i] > nums[i + 1]:
            return 'no'
         
    return 'yes'
    
  
nums = [20, 21,34,56,78]
arr = [15,15,67,89,89,100]
arrs = [26,666,4,5,77,8,33]
arrayss =[]
numbers = [5]

print(isSorted(nums))
print(isSorted(arr))
print(isSorted(arrs))
print(isSorted(arrayss))
print(isSorted(numbers))
            