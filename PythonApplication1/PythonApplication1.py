def cube(getal):
    return getal**3


x = 2
cubex = cube(x)
print("de derde macht van", x, "is", cubex)


def sqrt(getal):
    return getal**0.5


print(f"de vierkantswortel van {x} is {sqrt(x)}")


def divide_by_four(input_number):
    return input_number / 4


print(divide_by_four(x))


def age_check(age):
    if age >= 13:
        return True
    else:
        return False


if age_check(x) == False:
    print("leeftijd!")

if age_check(47):
    print("47 jaar")

# a python list begins and ends with square brackets [ and ]
# Each item is separated by a comma ,

# Use modulo % to calculate the remainder of a division.
# Python is zero based.

l = ["Jan", "Piet", "Joris", "Korneel"]
print(l[1:3])
print(len(l[1:3]))

l2 = [45, 55, 8, 4]
zipped = zip(l, l2)
print(list(zipped))
# [('Jan', 45), ('Piet', 55), ('Joris', 8), ('Korneel', 4)]

# Range function creates a list of consecutive numbers.
my_list = range(10)
print(my_list)
# range(0, 10)

print(list(my_list))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(1, 100, 10)
print(list(my_range))
# [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

fruits = ["apple", "banana", "cherry", "date"]

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = names.sort()
print(names)

print(sorted(fruits))

# Select the last element of the list
last = fruits[-1]
print("Last element:", last)

words = ["@coolguy", "#nofilter", "@kewl", "reply"]
usernames = []
for word in words:
    if word[0] == "@":
        usernames.append(word)

print(usernames)

l1 = [1, 2, 3]
l3 = [10, 20, 30]
l4 = l1 + l3
print(l4)

l5 = l4 * 2
print(l5)  # [1, 2, 3, 10, 20, 30, 1, 2, 3, 10, 20, 30]

l6 = [2 * x for x in l1]
print(l6)
