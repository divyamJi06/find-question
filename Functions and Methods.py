#method ?? --> function starts with a . (lame definition)
#function is a word followed by parenthesis
#len function
#clear
#get method
d = {"1":1,"2":2,"3":3,"4":4}
#d.get(key) --> d[key]
print(d.get("1"),d["1"])

#d.update method --> used to merge two dictionaries

d1 = {"Name":"Ayush","Place":"Blore","Mob":"9513853298","Phone":"Same"}
d2 = {"Name":"Fouzan","Loc":"India","Phone":"9876543210"}
d1.update(d2)
#same keys replacing values and new key gets added 
print(d1)
print(d2)

#three methods that return sequence data type
#lists/tuples --> dictionary using zip or dict
#dictionary --> lists/tuples

#method to get all the keys
a = d1.keys() #use list or tuple function to convert 
print(a) 
#method to get all the values
a = d1.values()
print(a)
#to get items 
a = d1.items() # a sequence of tuples
print(a)

