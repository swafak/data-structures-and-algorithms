def missing(nums):
    
    n = len(nums)
    
    nums.sort()
    
    for i in range(n-1):
        
        if nums[i + 1] != (nums[i] + 1):
            return nums[i] + 1
    
    return nums[n-1] + 1  

nums = [1,2,3,5]
arr = [8,2,4,5,3,7,1]
arrs =[1]

print(missing(nums))
print(missing(arr))
print(missing(arrs))
        
    
