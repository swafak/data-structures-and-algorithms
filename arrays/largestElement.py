def largestElement(nums):
    
    maxV = 0
    
    for i in range(len(nums)):
        for j in range(len(nums)- 1):
            
            if nums[i] < nums[j]:
                maxVa = nums[j]
            else:
                maxVa = nums[i]
            
            maxV = max(maxV,maxVa )
            
    return maxVa

def largest(arrs):
    return max(arrs)
    
arr = [10,60,4]
    
print(largestElement(arr))
print(largest(arr))