#list is mutable and orders sequence and allows duplicates

mahesh = [1, 2, "mahesh"]
mahesh.append("ravuri")
print(mahesh[2])
mahesh.insert(1, 2)
print(mahesh)
print(mahesh[1:4])

#touple is immutable. means, we cann't chnage the values once we declared in the touple
#this is also store values in order and allows duplicates

ravuri = (1,3, "mahesh")
print(len(ravuri))
print(ravuri[2])

#dictionary is form of key value pairs. it's unorder pair
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Dictionary items are ordered, changeable, and do not allow duplicates.

my_dict = {1:"mahesh", 2:"ravuri", "c":"maheshravuri"}
print(my_dict[2])
print(my_dict["c"])
dic = {}
dic["firstname"] = "mahesh"
dic[2] = "ravuri"
print(dic)

#set is also immutable but you can remove items and add new items. and it stores values in unordered and not allows diplicates

my_set = {"maheh", "apple", "mango"}
print("apple" in my_set)
#to remove item from set use discard() method
#if you want to add use add()
#if you want to update use update()
#There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.
#
# The intersection() method keeps ONLY the duplicates.
#
# The difference() method keeps the items from the first set that are not in the other set(s).
#
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
n = {}
v = {1,4,7}
b = set(range(8))
print(b)

d = b.symmetric_difference(v)
print(d)
