#arthimetic operators
a = 5 
b = 7
print (a+b)
print(a-b)
print(a/b)
print(a*b)
print(a|b)
print(a**b)
print(a//b)
print(a%b)


#logical operators
# and or not are logical operators

# and
print(True and True)            #true
print(True and False)           #false
print(False and True)           #false
print(False and False)          #false

# OR
print(True or True)   #true
print(False or False)  #false
print(True or False)    #true
print(False or True )    #true

#not
print(not False ) #true
print(not True)    #true

# RELATIONAL OPERATORS
# >,<,>= , <= , != , == Are relational operators

print(5>2)   #true
print(2>9)   #true
print(2<9)    #true

print(3 >= 3)   #true
print(4 != 2)   #true
print(4 != 4)   #false
print(5 == 5)   #true

#assignment operator 
# = , +=, -=, *= are the asssignment operators

a = 1
a = a + 1
print(a)  #2

a  += 1
print(a) #3

a -= 1
print(a)  #2

# membership operator
# "in" and "not in" are the membership operator
# result of membership operators are in boolean (true and false)
# checks whether an element is a member of iterable
#iterable means sequence of data, list , tuple etc are iterables data

vowels = ["a","e","i","o","u"]
print("b" in vowels) # false
print("b" not in vowels) #true

print("e" in vowels)  #true
print("a" not in vowels)  # false

# identity operators
#"is" and "is not" are the identity operators
#they check whether two identities are same obj or not

a = 1 
b = 1
print (a is b) #true
print(a is not b) #false

a = []
b = []
print (a is b) #both obj are not same obj. false
print (a is not b) #true