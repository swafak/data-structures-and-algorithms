
def quick_sort(values):
    if len(values) <= 1:
        return values
    
    pivot = values[0]
    less_than_pivot =[]
    more_than_pivot =[]
    
    for value in values[1:]:       
        
        if value <= pivot:
            less_than_pivot.append(value)
            
        else:
            more_than_pivot.append(value)
            
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)
    
numbers = [4,7,39,5,85,6,2,9,8]
num =[3,7,2,8]
 
print(quick_sort(numbers))
print(quick_sort(num))
