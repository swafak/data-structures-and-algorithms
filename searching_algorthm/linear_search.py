def linear_search(list, target):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not in the list")
        
        
numbers = [0,1,2,3,4,5,67,8,9,68,345,67645,344556,7677,7,8,89,9,99,76]
result = linear_search(numbers, 99)

verify(result)


