def isAnagram( s, t):
    sort_s =sorted(s)
    sort_t = sorted(t)

    return sort_s ==sort_t


s= "anagram"

t = "margana"

a ="bottle"
b ="bottl"

result =isAnagram(s,t)
print(result)

print(isAnagram(a,b))