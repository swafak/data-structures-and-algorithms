def binary_search(list, target):
    
    first = 0
    last = len(list) - 1
  
    
    while first <= last:
        midp = (first + last)//2
       
    
        if list[midp] == target:
            return midp
        elif list[midp] <  target:
            first = midp + 1
        else:
            last = midp - 1
    
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not in the list")
            
        
        
numbers = (4,6,7,8,9)

result =binary_search(numbers,9)

verify(result)