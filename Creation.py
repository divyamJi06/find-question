#dictionary is a mapping --> similar to functions in math --. mapping inside {}

dic = {10:-10,9:-9,8:-8,7:-7}
#here all items before : are keys and after the : are values

#{ --> marks the opening of a dict and } --> end of a dict
#each key is assigned to the value by a colon --> key:value
#and each key:value pair is seperated by a comma
#the key should be an immutable data type and should be unique , you cannot have one key pointing to two different values.




# one - one mapping, one -many mapping, many-one mapping and many-many mapping
#one-one and one-many are allowed
print(dic)
print(type(dic))

#dict are mutable
dic[6] = -6
print(dic)
#here we assigned a value to uncreated key or index
#but this doesn't work with lists
a = [1,2,3,4]
#a[4] = 0 --. IndexError


#creating dictionaries using lists
key_list = [10,9,8,7,6,5,4,3,2,1]
value_list = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
#zip function is used to convert two lists into a dictionary
temp_dictionary = zip(key_list,value_list) #this creates a zip object
print(temp_dictionary)
#to convert zip object into dictionary we use the dict function
final_dictionary = dict(temp_dictionary)
print(final_dictionary)

#loops
dictionary = {}
for i in range(len(key_list)):
    dictionary[key_list[i]] = value_list[i]
print(dictionary)

