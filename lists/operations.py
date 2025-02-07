#Swap
a = [10,50,60,70,80]

a[0],a[4] =a [4],a[0]
print(a)

#size
n= len(a)
print(n)

#maximum
largest = max(a)
print(largest)

#minimum
smallest =min(a)
print(smallest)

#count element
count_10 = a.count(10)
print(count_10)

#check if element exist by count
if a.count(10) > 0:
    print("exists")
else:
    print("doesn't exist")

#Find index
print(a)
print(a.index(10))

# Syntax of List index() Method
# list_name.index(element, start, end) 
pos_70 = a.index(70,2,4)
print(pos_70)


#merge two lists
b= [1,3,5,6]
c = a + b
print(c)