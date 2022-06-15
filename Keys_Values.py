#Accessing keys and values
d = {10: -10, 9: -9, 8: -8, 7: -7, 6: -6, 5: -5, 4: -4, 3: -3, 2: -2, 1: -1}
for i in d:   #this prints the keys by default --> Traversing a dictionary
    print(i)
    
"""
for i,j in d:  #we're trying to unpack the key whih is integer here
    print(i,":",j)
"""

for i in d:
    print(i,":",d[i])

#.keys method and .values method
#.keys() and .values() by default gives a sequence data type 
keys = list(d.keys())
values = list(d.values())
print(keys,values)
"""
a = dict(keys,values)  # this methos fails
print(a)
"""