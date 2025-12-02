# Tuples: ordered, immutable, allows duplicate elements - ()
mytuple = tuple(["Max", 28, "India"])

print(mytuple)
print(type(mytuple))
print(mytuple[::-1])

# mytuple[0] = 'Kevin'
# print(mytuple) #Throws an error as its immutable
fruits = ('a','p','p','l','e')
print(fruits)
# print(fruit.count("x"))

my_tuple = "Max", "Kshirod", 22
first_name, name, age = my_tuple 

print(first_name)
print(name)
print(age)

another_tuple = (0,1,2,3,4,5,6,7,8,9)

i1, *i2, i3 = another_tuple

print(i1)
print(i2)
print(i3)