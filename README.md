# string_in_python
A string is a sequence of characters that represent textual data. 
String are created by enclosing a sequence of characters within quotes, either single quotation marks ‘’ , or double quotation marks ” ”.
Syntex: 
a =“String value” #is a same as ‘String value’
Example,
print(“hello”) #output : hello
print(‘hello’) #output: hello , is the same as print(“hello”)
#create a string 
string = “my first string value”
print(string) #output: my first string value 
We can assign a multiline string to a variable using three quotes. Syntax,  
A = “””line 1 
Line 2 
line 3”””
a = ‘“this my multiple lines, 
string ”’
print(a) “”” output: this my multiple lines,
string”””
iv -	Check existing variable in string: 
In python, we can check if a certain character is existing in a string by using keyword in. 
Syntax: 
if value in String: 
do 
Example, 
x=”hello!! you are in resume of python ”# makes a sentence an object by named x
a= “resume” # make a word an object by named a
if a in x: #condition to excute
print(‘yes its present’) #  to check
else: # incase insatisfaction of condition 
print( ‘no there’s not’) #what you have to do
Also, we can check if character is not present by using keyword not in. Example, 
x=”hello!! you are checking if that is actually working ”
a= “resume”
if a in not x: 
print(‘yes its present’) 
else: 
print( ‘no there’s not’)
Result: 
 
v -	 Slicing in string: 
In Python, slicing is method that returns a range of characters.
Syntax: 
sentence[ start_index : end_index, step]
specify the start index and the end index, and the step parameter is optional, by defaults step is equal to 1. Example, 
a = “hello!! My name is hatim ”
print( a[0:5]) #output: hello!
vi -	Modify a string:
In python, we can modify a string after creating it by recreating it again. Example, 
x = “hatim” 
print(x) #output: hatim 
x= “hat” # modify the value of x
print(x) #output: hat
vii -	upper() method:
The upper() method is a function that converts a string to uppercase and returns it. Example, 
a = “hello !! my name is hatim”
print(a.upper()) #output : HELLO!! MY NAME IS HATIM
viii -	lower() method: 
The lower() method is function that converts a string to lowercase and returns it. Example, 
a = “HELLO!! MY NAME IS HATIM”
print(a.lower()) #output : hello!! My name is hatim
ix -	strip() method to remove whitespace: 
The strip() method is function that removes any leading or trailing whitespace characters in string. Example,
a= “hello!!        My name       is      hatim    ”
print(a.strip()) #output : hello!! my name is hatim
x -	Capitalize() method:
The capitalize() method is function that converts a string to Capitalize ad returns it. Example
a = “hello!! my name is hatim ”
print(a) #output: Hello!! my name is hatim 
xi -	 Replace() method to replace in string: 
The replace() method is function that substituted character in string with another string. Example,
a = “hello !! my name is hatim”
print(a.replace(“h”,”j”))#output : jello!! my name is jatim
xii -	Split() method to split a string: 
The split() method is function that generates a list of substrings by using the specified separator to split the original string into individual items within the list. Example, 
a = “hello! my name is hatim, ”
print(a.split(“!”)) #output : [“hello”, “my name is hatim”]
xiii -	String concatenation: 
In python, concatenation, combination and join two or multiples strings together can be done by using the operator +. Example,
a=”hatim”
b=”benjebara”
print(a+’’ ”+b) #output : hatim benjebara
ps: +  is also mathematic operateur, don’t mix string with float or int.
xiv -	Format() method to string format: 
The format () method is function that print a combination of a string and numerical data. Example, 
age = “35” 
work = “data analyst”
number_phone = “00212674495530”
txt = “My name is hatim, and I am {} and I have {} years ago and this my number phone {}” 
print(txt.format(work, age, number_phone))
Result: 
My name is hatim, and I am data analyst and I have 35 years ago and this my number phone 00212674495530
Also, we can indice a position of variables by using a number of index. Example, 
print(“my number phone is {2}, I am {0} and I have {1}”.format(work, age, number_phone))
Result: 
my number phone is 00212674495530, I am data analyst and I have 35
xv -	Escape character: 
In Python, some character is not allow to use inside the string. However, we can print them by using an espace character (a backslash). 
List of not normal characters:  
•	\’ : single Quote
•	\\ : Backslash
•	\n: newline
•	\r : Carriage return
•	\t : tab
•	\b : backspace
•	\f : form feed 
•	\ooo : octal value
•	\xhh : hex value
xvi -	String methods: 
List of methods available for string in python:
•	captitalize(): Converts the first character to upper case.
•	casefold() : Converts string into lower case.
•	center() : Returns a centred string.
•	count(): Returns the number of times a specified value occurs in a string
•	encode(): Returns an encoded version of the string 
•	endswith() : Returns true if the string ends with the specified value
•	expandtabs(): Sets the tab size of the string
•	find() : Searches the string for a specified value and returns the position of where it was found 
•	format(): Formats specified values in a string.
•	format_map(): Formats specified values in string.
•	index(): Searches the string for a specified value and returns the position of where it was found.
•	isalnum(): Returns True if all characters in the string  are alphanumeric 
•	isalpha(): Return true if all characters in the string are in the alphabet 
•	isdecimal(): Returns true if all characters in the string are decimals 
•	isdigit(): Returns true If the string is an identifier
•	isidentifier(): Returns true if the string is an identifier 
•	islower(): Returns true if all characters in the string are lower case
•	isnumeric(): Returns true if all characters in the string are numeric
•	isprintable(): Return true if all characters in the string are printable
•	isspace(): Return true if all characters in the string are whitespaces
•	istitle(): Return true if the string follows the rules of a title
•	isupper(): Return true if all characters in the string are upper case
•	join(): Join the elements of an iterable to the end of the string
•	ljust(): Return a left justified version of the string
•	lower(): Converts a string into lower case 
•	istrip() : Returns a left trim version if the string 
•	maketrans() : Returns a translation table to be used in translations
•	partition(): Returns a tuple where the string is parted into three parts 
•	replace(): Returns a string where a specified value is replaced with a specified value
•	rfind(): Searches the string for a specified value and returns the last position of where it was found 
•	rindex(): Searches the string for a specified value and returns the last position of where it was found 
•	rjust(): Returns a right justified version of the string 
•	rpartition(): Returns a right justified version of the string 
•	rsplit() : Return the right trim version of the string 
•	split() : Splits the string at the specified separator, and returns a list
•	splitlines(): Splits the string at line breaks and returns a list 
•	startswith(): Returns true if the string with the specified value
•	strip(): Returns a trimmed version of the string 
•	swapcase(): Swaps cases, lower case becomes upper case and vice versa 
•	title(): Converts the first character of each word to upper case 
•	translate(): Returns a translated string
•	upper() : Converts a string into upper case
•	zfill(): Fills the string with a specified number of 0 values at the beginning 
