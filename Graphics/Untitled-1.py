'''
#dictionary

d1 = {"Shreya" : "Chicken", "Sutrishna" : {"B" : "Roti", "L" : "Paneer", "D" : "Vegtables"}}
print (d1["Sutrishna"]["L"])
'''
Baba = d2 = {"B":"Tea","B":"Roti","L":"Rice","D":"rice"}
print(Baba["B"])


'''
#getting driving licence

print("enter your age: ")
age = int(input())
if  age<100 or age>7:
    print("You can not drive")
elif age<18:
    print("You can not get driving Licence!")
elif age==18:
    print("we will think about it")
else:
    print("You can get a licence")
'''

'''
#list
list1 = ['shreya', 'suman', 'shruti']
for item in list1:
    print(item)
'''

'''
#dictionary by user defined system
d1 = {"aboundond":"uninhabited","contraception":"precaution"}

print("enter a word you want to know: ")
n1 = input()
print(d1[n1])
print("thanks")
'''
'''
#faulty calculator
tup1 = ("1","2","3","4")
comp1 = input()
if comp1 in tup1:
    print("Enter first value")
    val1 = int(input())
    print("Enter second value")
    val2 = int(input())
    if comp1 == "1":
        if (val1 == 56 and val2 == 9) or (val1 == 9 and val2 == 56):
            print("Result is 77")
        else:
            print("Result is", val1 + val2)
    elif comp1 == "2":
        print("Result is", val1 - val2)
    elif comp1 == "3":
        if (val1 == 45 and val2 == 3):
            print("Result is 555")
        else:
            print("Result is", val1 * val2)
    else:
        if (val1 == 56 and val2 == 6):
            print("Result is 4")
        else:
            print("Result is", val1 / val2)
else:
    print("Invalid computation option, please rerun the program")
print("Thanks for using my calculator")
'''

'''
#string
mystr = "Harry is a good boy"
# print(len(mystr))
# print(mystr[::-2])

print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))
'''
'''
# String Functions:

demo = "Aakash is a good boy" 
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is")
print(demo.find("good","nice"))
'''

'''
#list
list1 = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]

# List Methods :
l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
print(l1)

l1.sort()
print(l1)      #l1 after sorting
l1.reverse()
print(l1)      #l1 after reversing all elements

[]                                             # list with no member, empty list
[1, 2, 3]                                    # list of integers 
[1, 2.5, 3.7, 9]                           # list of numbers (integers and floating point)
['a', 'b', 'c']                               # lisst of characters
['a', 1, 'b', 3.5, 'zero']                # list of mixed value types
['One', 'Two', 'Three']               # list of strings 

'''
'''
a = {'key', 'value', 'cow':'mooh'}
print(a['cow'])
#will print "mooh" on the screen

# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())
'''
'''
#set
s = set()
# print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1))
'''
'''
#conditional opetators
# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# Quiz
print("What is your age?")
age = int(input())
if age<18:
    print("You cannot drive")

elif age==18:
    print("We will think about you")

else:
    print("You can drive")
'''
'''
dict1= {"Best Python Course": "CodeWithHarry",
        "Best C Languge Course": "CodeWithHarry",
        "Harry Sir":"Tom Cruise Of Programming"
        }

for x,y in dict1.items():
    print(x, y)
'''
'''
# list1 = [ ["Harry", 1], ["Larry", 2],
#           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item
'''        
'''
#while loop

i = 0
while(i<45):
    print(i)
    i = i+1
'''
'''
i = 0
while(True):
    print(i+1, end=" ")
    if(i==44):
       break #to stop the loop
    i = i+1
'''
'''
while(True):
  inp = int(input("enter nummber: "))
  if inp>100:
    print("Congrats you have entered more than 100")
    break
  else:
    print("Try again)
    continue
'''
'''
#guessing game
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over") 
'''    
'''
# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function2.__doc__)
'''

'''
f = open("Shreya chakraborty.txt") #to open file #f is file pointer

r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file.
 
 Python has a built-in open() function to open a file.

The syntax of the function is:

open("filename" ,"mode")
To open a file, we must specify two things,

Name of the file and its extension
Access mode where we can specify in which mode file has to be opened, it could either be read (r), write (w) or append(a), etc. For more information regarding access modes, refer to the previous tutorial.
For Example, 

open("myfile.txt")
The file “myfile.txt” will open in "rt" mode as it is the default mode. But the best practice is to follow the syntax to avoid errors.

The open function returns a file object. We store this file object into a variable which is generally called as a file pointer/file handler. Here is a code snippet to open the file using file handing in Python,

  f=open("myfile.txt," "w")
You can use this file pointer to further add modifications in the file. An error could also be raised if the operation fails while opening the file. It could be due to various reasons like trying to access a file that is already closed or trying to read a file open in write mode.


 
How to read a file?

To read a file in Python, there are various methods available,
We can read a whole file line by line using a for loop in combination with an iterator. This will be a fast and efficient way of reading data.
When opening a file for reading, Python needs to know exactly how the file should be opened. Two access modes are available reading (r), and reading in binary mode (rb). They have to be specified during opening a file with the built-in open() method.
f = open("myfile.txt", "r")
The read() method reads the whole file by default. We can also use the read(size) method where you can specify how many characters we want to return i.e.

f.read(2); #Here, you will get the first two characters of the file.
You can use the readline() method to read individual lines of a file. By calling readline() a second time, you will get the next line.
readlines() method reads until the end the file ends and returns a list of lines of the entire file. It does not read more than one line.       
f=open("myfile.txt","r");
f.readlines() #Returns a list object
Note: The default mode to read data is text mode. If you want to read data in binary format, use ''rb".

Is it necessary to close a file?

The answer is yes, it is always the best practice to close a file after you are done performing operations on it. However, Python runs a garbage collector to clean up the unused objects, but as good programmers, we must not rely on it to close the file. Python has a build-in close() function to close a file i.e;

f.close()
I hope you like this tutorial. Here, we have discussed different file handling in Python with examples that will help you while working on real-world projects.

Source Code:
f = open("harry.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()


'''

'''
MODES

PURPOSE

“w” mode:

 

Here “w” stands for write. After opening or creating a file, a function, f.write() is used to insert text into the file. The text is written inside closed parenthesis surrounded by double quotations. There is a certain limitation to the write mode of the opening file that it overrides the existing data into the file. For a newly created file, it does no harm, but in case of already existing files, the previous data is lost as f.write() overrides it.  

 

“a” mode:

 

“a” symbolizes append mode here. In English, appends mean adding something at the end of an already written document, and the same is the function the mode performs here. Unlike write mode, when we use "a" keyword, it adds more content at the end of the existing content. The same function i.e., f.write() is used to add text to the file in append mode. It is worth noting that append mode will also create a new file if the file with the same name does not exist and can also be used to write in an empty file.

 

“r+” mode:

 

At the beginning of the description, I told you that we would learn reading and writing a file simultaneously. Well, r+ mode is more of a combination of reading and append than read and write. By opening a file in this mode, we can print the existing content on to the screen by printing f.read() function and adding or appending text to it using f.write() function.

 

A very helpful tip for beginners:
If you are writing in append mode, start your text by putting a blank space or newline character (\n) else the compiler will start the line from the last word or full stop without any blank space because the curser in case of append mode is placed right after the last character. So, it is always considered a good practice to adopt certain habits that could help you in the future, even though they are not much helpful now.

f.close():
f.close() is used to close a file when we are done with it. It is a good practice to close a file after use because whichever mode you opened it for, the file will be locked in for that specific purpose and could not be accessed outside the program, even though the file browser.

Code file as described in the video
# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("harry2.txt", "r+")
print(f.read())
f.write("thank you")

'''

