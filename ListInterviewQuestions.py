a = [1, 2, 3, 4, 5]

# slice [start:end:step]

print(a[3:0:-1])
print(a[-1:-5:-1])
print(a[0:4:1])
print(a[::-1])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v


print(fun(data[0]))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])
print(a[:6:2])
print(a[:7:2])

a[::2] = 10, 20, 30, 40, 50
print(f"this is crazy:{a}")
# below will throw an exception ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# a[::2] = 10, 20, 30, 40, 50, 60

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']

fruit_list2 = fruit_list1

fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0

for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)


def f(value, values):
    v = 1
    values[0] = 44


t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

import random

fruits = ['apple', 'banana', 'papaya', 'cherry']

random.shuffle(fruits)

print(fruits)
