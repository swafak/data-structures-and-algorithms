
def two_sum(nums, target):
    num_map = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        print(num_map)
    return []

nums = 2,11,15,17,7
target = 9

result = two_sum(nums, target)

print(result)


#optimal solution
#O(n) linear time complexity and space complexity
