#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[ ]:


Num = 10

print(type(Num))


# ##### Assinging float

# In[ ]:


Num = 10.5
print(Num)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 + Num2
print(Sum)

Sum += 2
print(Sum)


# ##### Subtraction

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 - Num2
print(Sum)

Sum -= 5
print(Sum)


# ##### Multiplication

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 * Num2
print(Sum)

Sum *= 5
print(Sum)


# ##### Division

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 / Num2
print(Sum)

Sum /= 5
print(Sum)


# ##### Floor Division

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 // Num2
print(Sum)

Sum //= 5
print(Sum)


# ##### Modulo

# In[ ]:


Num1 = 10
Num2 = 5

Sum = Num1 % Num2
print(Sum)

Sum %= 5
print(Sum)


# ##### Exponential

# In[ ]:


Sum = 10 ** 5
print(Sum)

Sum = 5

Sum **= 5
print(Sum)


# ### String Input-Output

# ##### String Assignment

# In[ ]:


Name = "Cao"
Name2 = "Wei"

print(Name)
print(Name2)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[ ]:


print("Hello World!")

print(Name)

print(Name, Name2, "Hello!", "Goodbye!")

print(Name, end=' Cao\n')
print(Name2)


# ##### String Concatenation

# In[ ]:


NameLast = "Liu"
NameFirst = "Bei"

NameFull = NameLast + " " + NameFirst

print(NameFull)

#Shorthand
NameFull += "!"
print(NameFull)


# ##### Type Conversion

# In[ ]:


Num = "15"
print(type(Num))

Num = int(Num)
# Num = str(Num)
# Num = float(Num)

Num *= 5
print(Num)


# ##### input()

# In[ ]:


Age = int(input("What is your age? "))
Age2 = int(input("Whatis your friend's age? "))

AgeAvg = (Age + Age2) / 2

print(AgeAvg)


# ##### format()

# In[ ]:


Age = 20
Name = "Sun Ce"

# W/ String Concatenation
print(Name + " is " + str(Age) + " years old before.")

# W/ F Strings
print(f"{Name} is {Age + 20} years old now.")


# ##### Old Way (python 2)

# In[ ]:





# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[ ]:


color = input('What is the color of the computer: ')
year = input('and what is the year it was released: ')
make = input('Who made this computer: ')
model = input('What is the model:')

print(f"That {year} {color} {make} {model} is cool.")

### If Statements
# In[ ]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 50
num2 = 51

if num1 == num2:
    print("They're the same")
if num1 >= num2:
    print("Number 1 is greater!")
if num1 <= num2:
    print("Number 1 is smaller")
    
    
is_round = False
is_red = False

if is_round or is_red:
    print("The ball is red or round.")


# ##### 'is' keyword

# In[ ]:


# num3 = 30

# if num3 is 30:
#     print("They're the same.")


# ##### 'in' keyword

# In[ ]:


numbers = [1, 2, 3, 4, 5, 6]

if 6 in numbers:
    print("That number is here.")


# ##### 'not in' keyword'

# In[ ]:


a_str = "Christopher"

if "Christ" in a_str:
    print("It is!")


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[ ]:


a_str = input('Enter Sentence here: ')

if "p" in a_str:
    print("This sentence contains the letter P.")
    
else:
    print("This sentence does not contain the letter P.")


# ## Using 'and'/'or' with If Statements

# In[ ]:


# Done above


# ### Elif Statements

# In[ ]:


num1 = 49
num2 = 50

if num1 == num2:
    print("They're the same!")
    
elif num1 >= num2:
    print("Number 1 is greater than or equal to!")
    
else:
    print("Number 2 is greater than or equal to!")


# ### Else Statements

# In[ ]:


# See above


# ### For Loops

# In[ ]:


name = "Wai Gong"

for x in name:
    print(x)
    
num = [1, 2, 3, 4, 5]

for y in num:
    print(y)
    
fruits = ["Banana", "Apple", "Pear"]

for fruit in fruits:
    print(fruit)
    
for i in range(1,11):
    print(i)


# ##### Using 'in' keyword

# In[ ]:


# see above


# ##### Continue Statement

# In[ ]:


# will continue to next iteration


# In[ ]:


for i in range(1,11):
    if i !=5:
        print(i)
        
for i in range(1,11):
    if i ==5:
        continue
        
    print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[ ]:


for i in range(1,11):
    if i ==5:
        break
        
    print(i)
    
fruits = ["Banana", "Apple", "Pear"]

for fruit in fruits:
    if fruit == "Apple":
        break
    
    print(fruit)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[ ]:


for i in range(1,11):
    pass
    # Eventually I want to write this code.


# ##### Double For Loops

# In[ ]:


fruits = ["Banana", "Apple", "Pear"]

for fruit in fruits:
    for i in fruit:
        print(fruit, i)


# ### While Loops

# In[ ]:


# num = 0
# while num < 10:
#     num += 1
#     print(num
          
# num = 0
# while num < 10:
#     num += 1
#     print(num)

# num = 11
# while num != 10:
#     num += 1
#     print(num)
    
user_input = ""

while user_input != "quit":
    user_input = input("Quit or continue?")


# ##### Looping 'While True'

# In[ ]:


while True:
    print("Looping")
    
    user_input = input("Quit or continue?")
    
    if user_input == "quit":
        break


# ##### While & For Loops Used Together

# In[ ]:


while True:
    print("Looping")
    
    user_input = input("Quit or continue?")
    
    if user_input == "quit":
        break
    else:
        number_input = int(input("Choose a number!"))
        
        for i in range(number_input):
            print(i)


# ### Built-In Functions

# ##### range()

# In[ ]:


# range(start, stop, step)
for i in range(0, 100, 2):
    print(i)
    
for x in range(5):
    print(x)


# ##### len()

# In[ ]:


print(len("Cao Cao"))

print(len(["Apple", "Banana", "Pear"]))


# ##### help()

# In[ ]:


help(help)


# ##### isinstance()

# In[ ]:


isinstance(4.5, float)


# In[ ]:


isinstance(4, float)


# In[ ]:


isinstance(4, int)


# In[ ]:


isinstance(32, str)


# In[ ]:


isinstance("32", str)


# ##### abs()

# In[ ]:


abs(-5)


# In[ ]:


abs(5)


# ### Try and Except

# In[ ]:





# ### Lists

# ##### Declaring Lists

# In[ ]:





# ##### Indexing a List

# In[ ]:





# ##### .append()

# In[ ]:





# ##### .insert()

# In[ ]:





# ##### .pop()

# In[ ]:





# 
# ##### .remove()

# In[ ]:





# ##### del()

# In[ ]:





# ##### Concatenating Two Lists

# In[ ]:





# ##### Lists Within Lists

# In[ ]:





# ##### Looping Through Lists

# In[ ]:





# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[ ]:


for x in range(0, 100):
    if x **3 > 1000:
        break
        
    print(x **3)


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[ ]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break
for x in range(1, 101):
   if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           print(x)


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[ ]:


age = int(input("How old are you?: "))
    
if age < 18:
    print("Kid")
    
elif age > 65:
    print("Senior")
    
else:
    print("Adult")


# In[ ]:




