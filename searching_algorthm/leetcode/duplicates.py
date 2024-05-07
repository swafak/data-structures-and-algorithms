def containsDuplicate(nums):
    num = set()
    for i in nums:
        if i in num:
            return True
        num.add(i)
    return False
    
numbers = [1,1,1,3,3,4,3,2,4,2]
no = [1,2,3,4]
letters =["A","B","C","D"]


print(containsDuplicate(numbers))
print(containsDuplicate(letters))
print(containsDuplicate(no))
