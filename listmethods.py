# what are methods?
# those functions which are defined inside the class are called methods

#functions
# -- build in function --
# --user defined function--
# --built in methods(those functions which are already defined in python class)--
# --user defined methods (theses function which are defined inside user-defined class)--

# list methods

# append()
a =[1,2,3]
a.append(4)
print(a)  # a=[1,2,3,4]

#extend()
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)  #[1,2,3,4,5,6]

#insert
vowels = ['a','e','o','u']
r = vowels.insert(2,"i")
print(r)  #[]
print(vowels) #["a","e","i","o","u"]

#index
vowels = ['a','e','i','o','u']
result=vowels.index('i')
print(result)  #2

#remove()
vowels = ['a','e','i','o','u']
print(vowels.remove('o'))
print(vowels)   #["a","e","i","u"]
vowels.remove("z") #error

#pop()
vowels = ['a','e','i','o','u']
result = vowels.pop()
print(vowels)  #vowels = ['a','e','i','o']
print(result)  #"u"

vowels = ['a','e','i','o','u']
result = vowels.pop(3)
print(vowels)  #vowels = ['a','e','i','u']
print(result)  #"0"

#count
data=[1,3,4,5,7,8,9,1,4,1,6,1,9,1,0,5,1,1,1]
result=data.count(1)
print(result) #8

#clear
data=[1,3,4,5,7,8,9,1,4,1,6,1,9,1,0,5,1,1,1]
data.clear()
print(data) #[]

#copy 
a = [1,2,3]
b=a
print(a==b)  #true
print(a is b) #true

b=a.copy()
print(a==b)  #true
print(a is b)  #false
# concept of shallow copy and deep copy
a = [1,2,[4,8]]
b=a.copy()
a[2][1]=7
print(a)  #[1,2[4,7]]
print(b)  #[1,2[4,7]]


# deepcopy
from copy import deepcopy
b = deepcopy(a)
a[2][1] = 9
print(a)  #[1,2[4,9]]
print(b)  #[1,2[4,8]]

#sort
a= [5,6,8,9,1,4]
a.sort()
print(a)  #[1,4,5,6,8,9]
a.sort(reverse= True)
print(a)  #[9,8,6,5,4,1]

#reverse
a= [5,6,8,9,1,4]
a.reverse()
print(a)  # [4,1,9,8,6,5]