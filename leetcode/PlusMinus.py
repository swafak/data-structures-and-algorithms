#Positive , negative and zero proportions /ratios

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
  
    for i in arr: 
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
          
    positive_ratio = positive / n
    negative_ratio = negative / n
    zero_ratio = zero / n
  
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}") 
    
    
#test
arr = [-4,-9,0,3,4,6,7]
plusMinus(arr)