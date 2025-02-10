# O(n) Time and O(1) Space
def secondL(nums):
    
    n = len(nums)
    
    largest = -1
    second = -1
    
    for i in range(n):
        if nums[i] > largest:
            
            largest = nums[i]           
    
    for i in range(n):
        if nums[i]>second and nums[i] != largest:
            
            second = nums[i]
            
    return second
            
#  One Pass Search – O(n) Time and O(1) Space
# expected method
def secondLarge(nums):
    largest = -1
    second = -1
    
    n = len(nums)
    
    for i in range(n):
        if nums[i] > largest:
           second = largest
           largest = nums[i]
            
            
        elif nums[i] < largest and nums[i] > second:
            second = nums[i]
    return second

# Using Sorting – O(n*logn) Time and O(1) Space
def secondLargest(nums):
    
    nums.sort()
    n = len(nums)
    for i in range(n-2,-1,-1):
    
        if nums[i] != nums[n-1]:
            return nums[i]
    
    return -1

nums = [3,4,57,6,8,8,8,9,30]
print(secondLargest(nums))
print(secondL(nums))
print(secondLarge(nums))


    