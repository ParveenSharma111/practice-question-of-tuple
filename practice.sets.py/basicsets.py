# thisset = set(("apple", "banana", "cherry"))
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# # for x in thisset:
# #     print(x)
# print("banana" in thisset)
# print("banana" not in thisset)



# add an items
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("apple")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("mango")
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1) 


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set2.difference(set1)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set = {"red" , "green" , "blue"}
# set.add("yellow")
# # set.discard("green")
# print(len(set))
# print(set)



# # Check whether 30 exists in this set:
# set = {10, 20, 30, 40, 50}
# # print(len(set))
# num = int(input("Enter a no:"))
# if num in set:
#     print("Number is present")
# else:
#     print("Number is not present")


# Add 60 to the following set:

# numbers = {10, 20, 30, 40, 50}
# numbers.add(60)
# print(numbers)


# numbers = {10, 20, 30, 40, 50}
# numbers.remove(20)
# print(numbers)

# numbers = {10, 20, 30, 40, 50}
# for x in numbers:
#     print(x)

    
# numbers = set([1, 2, 2, 3, 4, 4, 5])
# print(numbers)


# union and intersection
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.union(set2)
# print(set3)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.intersection(set2)
# print(set3)


# difference = no of element set1 are differ frome set2
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.difference(set2)
# print(set3)


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {1 , 2 ,3 , 4 , 5}
# set1.clear()
# print(set1)


# set1 = {1, 2, 3,}
# set2 = {3, 1 , 2}
# # if set1==set2:
# #     print("both set are equal")
# # else:
# #     print("both are not equal")
# or
# print( set1 == set2 )



# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# y = set2.issubset(set1)
# print(y)

# numbers = set([1, 2, 2, 3, 4, 4, 5, 5, 6])
# print(numbers)

# fruits1 = {"apple", "banana", "orange"}
# fruits2 = {"banana", "mango", "orange"}
# print(fruits1.intersection(fruits2))


# numbers = {45, 12, 89, 23, 67, 5}
# smallest = min(numbers)
# largest = max(numbers)
# print("Smallest no. is:", smallest)
# print("Largest no. is:",largest)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Write a program that prints:

# Union
# Intersection
# Difference of A and B
# Difference of B and A
# Symmetric difference

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))