def selection_sort(values):
    sorted_list=[]
    
    for i in range(0, len(values)):
        index_pop = min_value(values)
        sorted_list.append(values.pop(index_pop))
    return sorted_list


    
def min_value(values):
    min_index= 0

    for i in range(1,len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
    

numbers = [4,5,6,87,890,2,45]
    
                
        
result = selection_sort(numbers)

print(result)
