#testing list
list = [1, 2, 3, 4, 5, 6]

# list comprehension
list0 = [x*2 for x in list]
print(list0)
print("\n")
list1 = [x * 2 for x in list if x < 3]
print(list1)
print("\n")
list2 = [x ** 2 for x in list if x % 2 == 1]
print(list2)

