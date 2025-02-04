def duplicates(num):
    nums = set()
    
    for i in range(len(num)):
        if num[i] in nums:
            return True
        
        nums.add(num[i])
        
    return False
    
# Same time complexity O(n), but set uses less memory than a dictionary in Python. 
def duplicate(nums):
    
    hmap = {}

    for i in range(len(nums)):
        if nums[i] in hmap:
            return True  
            
        hmap[nums[i]] = True 
    return False  
    
    
# brute force
# Time Complexity: O(n log n) (Due to sorting)
# Space Complexity: O(1) (In-place sorting)

def dup(nums):
    
    nums.sort()
    for i in range(len(nums)- 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
    
numbers = [1,1,1,3,3,4,3,2,4,2]
no = [1,2,3,4]
letters =["A","B","C","D"]

print(dup(numbers))
print(dup(letters))
print(dup(no))

print(duplicate(numbers))
print(duplicate(letters))
print(duplicate(no))


