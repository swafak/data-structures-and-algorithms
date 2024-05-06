def merge_sort(values):
    if len(values) <= 1:
        return values
    
    mid = len(values)//2
    
    left_values = merge_sort(values[:mid])
    right_values = merge_sort(values[mid:])
    sorted_values = []
    
    left_index =0
    right_index =0
    
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index  += 1
            
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    
    return sorted_values

numbers = [3,90,34,6,77,8,56,2,3,5,7,9,96,9,65,3,3,25,4,5,6,6,7]

print(merge_sort(numbers))