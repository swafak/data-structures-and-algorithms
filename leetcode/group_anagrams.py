from collections import defaultdict

def groupAnagrams(strs):
    
    map = defaultdict(list)
    
    for i in strs:
        sorted_word ="".join(sorted(i))
        map[sorted_word].append(i)
        
    return list(map.values())


#test cases
a = ["eat","tea","tan","ate","nat","bat"]
b = [""]
c = ["a"]


print(groupAnagrams(a))
print(groupAnagrams(b))
print(groupAnagrams(c))

