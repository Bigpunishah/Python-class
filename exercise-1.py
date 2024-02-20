print("=====================================")
print("  COP 2047 02Z Spring 2023 Python ")
print("    exercise 1  Input Process Output ")   # <-- title of assignment
print("         'Vikel Cunningham' ")  # <-- put your name here!
print("=====================================")
print()

print("In this first exercise you will use the input-process-output")
print("methodology to do a few simple things with numbers, strings, ")
print("and boolean variable types.  Read the accompanying word doc, ")
print("and then come up with a few examples of your own.")
print()
print("Write a few lines to test out simple ideas, and come up with ")
print("some examples of simple calculations. Use input prompts, do the ")
print("processing, and then use an output with appropriate labelling.")
print()
print()

#----- write some code here with examples of string I P O
#      use appropriate prompts on your inputs
#      label the output to help the user  know what it means
#      this can be as simple as hello [name]
name = "Vikel"
school = "Eastern Florida State College"
major = "Software Development"
print("Hello my name is " + name + ", I am currently enrolled at" + school + ". I am majoring in, " + major + ".")
#Hello my name is Vikel, I am currently enrolled atEastern Florida State College. I am majoring in, Software Development.


#the print would be the oputput & assigning the string with specfic names like 'name', 'school', 'major' they allow me to make seperate
#adjustments instead of going in and manually changing my name or school or even major. It saves a lot of time.


#----- write some code here with examples of numeric I P O
#      use appropriate prompts on inputs
#      use  labels for outputs
#      do some simple math such as distance = rate * time
#      or taxamount = totalsale * taxrate     totalamount = totalsale+taxamount
rate = 10
time = 5
distance = rate * time
print(distance)
#50

total = 20.99
tax = .06
amountDue = total * tax + total
print(amountDue)
#22.24



#---- write some code here which will set the value of some
#     variables to True or False and do a little processing,
#     and provide a final result as output.
a = 5
b = 5
 
print(a == b)
#true
print(a < b)
#false
print(a > b)
#false
