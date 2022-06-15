dic = {"one":1,"two":2,"four":4}
del dic["four"]
print(dic)
#del works only with mutable datatypes and is used for deleting variables
#checking for existance of a key
#membership operators check only for key in dictionaries.... Because key is unique
print("one" in dic and 4 in dic)