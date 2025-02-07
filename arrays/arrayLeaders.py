def arrayLeaders(nums):

    n = len(nums)
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] < nums [j]:
                break        
        else:
            result.append(nums[i])
    return result


nums =[16,17,4,3,5,2]
arr =[10,4,2,4,1]
arrs =[5,10,20,40]

print(arrayLeaders(nums))
print(arrayLeaders(arr))
print(arrayLeaders(arrs))
