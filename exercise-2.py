print("=====================================")
print("  COP 2047 02Z Spring 2023 Python ")
print("    exercise 2  Lists, Loops, Decisions ")   # <-- title of assignment
print("         'Vikel Cunningham' ")  # <-- put your name here!
print("=====================================")
print()

# as in the word doc, have some fun with lists!
# Try to do some looping, and throw in a little
# decision making for good fun. Amuse me!

list1 = [5, 10, 15, 20, 25]
list2 = [30, 35, 40]
print(list1 + list2)

names = ["Vikel", "Jay", "Cunningham"]
greeting = ["Hello", "Hi"]

print(greeting[0] + " " + names[0])

print(list2[-1])

a,b,c = names
print(c, b, a)

for a in list1:
    print( a)

for i in range(len(list2)):
    print(list2[i])

a = 25
b = 30
if b < a:
    print("b is less than a")
else:
    print("nah b isnt less than a")

if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("I am learning alot about python :)")

