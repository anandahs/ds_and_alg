# 1. create an array and traverse
import array

print("step1")
array1 = array.array("i", [1, 2, 3, 4])

for element in array1:
    print(element)

#2.  access individual elements through indexes
print("step2")
print(array1[2])

#3. append any value to the array using append() method, it adds element to last
print("step3")
array1.append(5)
print(array1)

#4. insert value into array using insert. insert will insert data at any index position
print("step4")
array1.insert(1, 10)
print(array1)

#5 extend array using extend() method
print("step5")
array2 = array.array("i", [20,21])
array1.extend(array2)
print(array1)

# add elements from list using from_list into arrays
print("step6")

temp_list = [30,31]

array1.fromlist(temp_list)
print(array1)

# remove any element from array using remove methodp
print("step7")

array1.remove(10)

print(array1)

# remove array element at the end using pop
print("step8")
array1.pop()

print(array1)

#fetch any element through its index using index() method
print("step9")
print(array1.index(30))

# reverse array using reverse method
print("step10")
array1.reverse()
print(array1)

# get array buffer information through buffer_info method
print("step11")
print(array1.buffer_info())

#get number of occurances of an element using count method
print("step12")
array1.append(1)
print(array1.count(1))

# convert array into toString()
print("step13")
array2 = array1.tostring()
print(array2)

#fromstrong is not available anymore

#convert array into python list with same elements using toList() method

array_to_list = array1.tolist()
print(array_to_list)

#slice elements of an array

print(array_to_list[:])
print(array_to_list[2:])
print(array_to_list[2:4])
print(array_to_list[:4])
print(array_to_list[-5:])
print(array_to_list[::-1])