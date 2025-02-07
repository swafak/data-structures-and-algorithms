def removeDuplicated(nums):
    
    n = len(nums)
    
    new = set()
    
    idx = 0
    
    for i in range(n):
        if nums[i] not in new:
            new.add(nums[i])
            nums[idx]= nums[i]
            idx +=1
    return idx
     
     
def removeDup(nums):
    n = len(nums)
    new = []
    
    idx = 0
    for i in range(n-1):
        if nums[i] not in new:
            if nums[i] == nums[i+1]:
                new.append(nums[i])
                idx += 1
    return new , idx
    
nums = [2, 2, 2, 2, 2]

print(removeDuplicated(nums))
print(removeDup(nums))