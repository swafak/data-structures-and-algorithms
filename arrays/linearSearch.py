def linearSearch(nums, target):
    
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1

arr = [1, 2, 3, 4]
x = 3

arrs =[10, 8, 30, 4, 5]
y = 5

ar = [10, 8, 30]
z = 6


print(linearSearch(arr, x))
print(linearSearch(arrs, y))
print(linearSearch(ar, z))