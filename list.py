# list are the mutable data type in python
# they are  the sequence of data inclosed within big brackets
# unlike array,the elements in list can be of heterogeneous datatypes
example = ['a',1,[2,3],"hello world"]

# creating a empty list
a = list()  # empty list[]
print(a)
a = []
print(a)   #[]

#creating a non empty list
a = [1,2,3]
print(a)

b = ['hello','world']
print(b)

c = [1,2,'hello',[4,5]] # list of mixed data types
print(c)

# Accessing the list elements
# list  elements can be accessed using indexing and slicing

#indexing
vowles = ['a','e','i','o','u']
print(vowles[3])  #  "o"
print(vowles[0])  #  "a"
print(vowles[11]) #  indexing error . list index out of order

#Negative indexing 
print(vowles[-1])  # "u"
print(vowles[4] == vowles[-1]) #true
print(vowels[-3])   #i

#slicing 
data = ["a","b","c","d","e","f","g","h","i","j"]

print(data[2:7]) #  data from 2 to 6 index are displayed ["c","d","e","f","g","h","i","j"]
print(data[:4])   # ["a","b","c","d"]
print(data[0:4])   # ["a","b","c","d"]
print(data[5:])  # ["f","g","h","i","j"]
print(data[1:9:2])  #["b" , "d" , "f" , "h"]
print(data[-8:-2])  #["c","d","e","f","g","h"]
print(data[9:1])  #[]
