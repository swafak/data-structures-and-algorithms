
def two_sum(num, target):
    
    hmap = {}
    
    for i in range(len(num)):
        compliment = target - num[i]
        if compliment in hmap:
            return [hmap[compliment], i]
           
        hmap[num[i]]= i
        # print(hmap)
    
    return []
        
nums = 2,11,15,7
target = 9

result = two_sum(nums, target)

print(result)

# print("next")

def two_sum(nums, target):
    num_map = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        # print(num_map)
    return []

numss = 2,11,15,7
targets = 9

resultss = two_sum(numss, targets)

print(resultss)


#optimal solution
#O(n) linear time complexity and space complexity
