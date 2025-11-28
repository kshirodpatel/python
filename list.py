# Lists: order,mutable, allows duplicate elements - []
mylist = [1,3,4,1,2,5,6,7,9,7,8]
mylist.append(89)
print(mylist)

mylist.pop()
print(mylist)

mylist.remove(7)
print(mylist)

mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)

# a = mylist[1:5]
# print(a)

b = [i*i for i in mylist]
print(b)
