print("hello") #same as print('hello')
a = '''this mmy multiple , 
lines'''
print(a)
#checking if the word existe in sentence
x = "hello!! you are in resume of python " # make a sentence an object and give it variable
a = "resume" # make a word an object and give it a variable
if a in x: 
    print(f"yes {a} is present") 
else: 
    print("no there no present in it ")
x="hello!! you are checking if that is actually working"
a= "resume"
if a not in  x: 
    print(f"no there's no existe of {a} in this sentence") 
else: 
    print("yes its existe ")

a = "hello, My name is hatim"
print(a[2:5]) 
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.strip())
print(a.replace("hatim", "maha"))
print(a.split(","))
a = "hatim"
b = "benjebara"
print(a+" "+ b)
age="35"
work = "data analyst"
number_phone = "00212674495530"
txt= "my name is hatim, and i am {} and i have {} years ago and this my phone number {}"
print(txt.format(work, age, number_phone)) # work only with string not int type
