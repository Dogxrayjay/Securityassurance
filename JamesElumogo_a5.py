# Application name: Study Review App

print("\n")
print ("Study_Revew_Quiz: Remember:")
print("\n")
thislist = ["1) Practice", "2) Makes", "3) Perfect"]
for x in thislist:
  print(x)
print("\n")
person = input('Enter your full-name: ')
print("\n")
print('Hello', person)
print("\n")
print("Greetings, lets get ready to pass this test with flying colors!")
print("\n")
Question = input ("Do you know what a data type is? 1 = Yes, 2 = No")
print("\n")
if Question == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("In computer science and computer programming, a data type or simply type is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data. Most programming languages support common data types of real, integer and boolean.")
print("\n")
Question1 = input ("Do you know what a string is? 1 = Yes, 2 = No")
print("\n")
if Question1 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation)")
print("\n")
Question2 = input ("Do you know what a Flow control statement is? 1 = Yes, 2 = No")
if Question2 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("Flow control is the management of data flow between computers or devices or between nodes in a network so that the data can be handled at an efficient pace.")
print("\n")
Question3 = input ("Do you know what a function is? 1 = Yes, 2 = No")
if Question3 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("In programming, a named section of a program that performs a specific task. In this sense, a function is a type of procedure or routine.")
print("\n")
Question4 = input ("Do you know what a Class is? 1 = Yes, 2 = No")
if Question4 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("a class is an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods)")
print("\n")
Question5 = input ("Do you know what an exception is? 1 = Yes, 2 = No")
if Question5 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("When an error occurs within a method, the method creates an object and hands it off to the runtime system. The object, called an exception object, contains information about the error, including its type and the state of the program when the error occurred. Creating an exception object and handing it to the runtime system is called throwing an exception.")
print("\n")
Question6 = input ("Do you know what an condition is? 1 = Yes, 2 = No")
if Question6 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("This is the ability to test a variable against a value and act in one way if the condition is met by the variable or another way if not. They are also commonly called by programmers if statements. To know if a condition is True of False, we need a new type of data: the booleans. They allow logical operations.")
print("\n")
Question7 = input ("Do you know what an variable is? 1 = Yes, 2 = No")
if Question7 == '1':
        print ("Awesome, keep up the good work!")
else:
        print (" a variable is a value that can change, depending on conditions or on information passed to the program. Typically, a program consists of instruction s that tell the computer what to do and data that the program uses when it is running.")
print("\n")
Question8 = input ("Do you know what an loop is? 1 = Yes, 2 = No")
if Question8 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("In computer programming, a loop is a sequence of instructions that is continually repeated until a certain condition is reached. Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.")
print("\n")
Question9 = input ("Do you know what an instruction is? 1 = Yes, 2 = No")
if Question9 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("an instruction is a single operation of a processor defined by the processor instruction set. The size or length of an instruction varies widely, from as little as 4-bits in some microcontrollers to many as multiples of a bytes in some very long instruction word (VLIW) systems.")
print("\n")
Question10 = input ("Do you know what an agrument is? 1 = Yes, 2 = No")
if Question10 == '1':
        print ("Awesome, keep up the good work!")
else:
        print ("Arguments are independent items, or variables, that contain data or codes. When an argument is used to customize a program for a user, it is typically called a parameter.")

        ## Add the space at end of the string in Python
print("\n")
result = input ('Please let me know if you learned something! Type Yes or No')
if result == 'Yes':
	print ('Im glad that you did')
else:
	print ('Lets try again')
print("\n")
choice = input ('Press q to quit')
if choice == 'q':
  sys.exit(0)
else:
  main()

	
