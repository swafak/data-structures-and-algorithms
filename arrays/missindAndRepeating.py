# def missingAndRepeating(nums):
    
#     n= len(nums)
#     nums.sort()
    
#     output =[]
#     missing = float('inf')
#     repeating = float('inf')
    
#     start = 1
    
#     for i in range(n-1):
#         print(start)      
#         if nums[i] != start :
#             missing = start
#             # output.append(missing)
            
#         if nums[i] == nums[i + 1]:
#             repeating = nums[i]
#             # output.append(repeating)
#         else:
#             start +=1
 
#     return repeating,missing
    
# nums = [2,2]   
# arr = [1,3,3,4] 
# arrs = [4,3,6,2,1,1]
# # print(missingAndRepeating(nums))
# # print(missingAndRepeating(arr))a
# print(missingAndRepeating(arrs))
        
            
            