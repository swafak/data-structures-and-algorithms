def two_sum(num, target):
    
    hmap = {}
    
    for i in range(len(num)):
        compliment = target - num[i]
        if compliment in hmap:
            return [hmap[compliment], i]
        
        hmap[num[i]]= i
    
    return []
        
nums = 2,7,11,15
target = 9

result = two_sum(nums, target)

print(result)