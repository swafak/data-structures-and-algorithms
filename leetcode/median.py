def find_median(arr):
  
    arr.sort()
   
    n = len(arr)
    
  
    if n % 2 == 1:  
        #odd
        median = arr[n // 2]
    else:  
        #even
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
          
    
    return median

# tests:
arr = [7, 1, 3, 4, 2, 6, 5]
print(find_median(arr))

arr2 = [7, 1, 3, 4, 2, 6]
print(find_median(arr2))


