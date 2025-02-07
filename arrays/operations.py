nums = [6,3,4,55,8,1,24,4,55,2]

# add to the end
nums.append(8)
print(nums)

#removes the first encounter of the item
nums.remove(4)
print(nums)

#remove by index
nums.pop(1)
print(nums)

#insert(index,item)
nums.insert(3,100)
print(nums)


#add multiple elements
nums.extend([89,90,56])
print(nums)

#sort
nums.sort()
print(nums)

#reverse
nums.reverse()
print(nums)


for i in range(len(nums)):
    print(nums[i], end=" ")