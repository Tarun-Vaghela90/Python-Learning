# primitive data Types
# integer    = whole  number  12346
#large  numbers   in define print(123_455_455)  it reads  123455455  but  dev to easy  to read
#float  number   1.456  or  12345.23
# boolean   True or False      /// advance  self note||  0  or 1


# print("hello"[4])
# print("hello"[-1]) #negative index   number is allowed

# print(123 + ""+ 123)



print(type("hello"))
print(type(123.45))
print(type(152))
print(type(True))

# type casting     //  changin int to string or  string to int

print(int("123") + int("456"))

int()
float()
str()
bool()

# excerice

# print("number of  letters in you name  is : " + str(len(input("enter your name\n"))))


# calution     + , - , * , / , //
print(4 - 3)
print(4 + 3)
print(4 * 3)
print(4 / 3)
print(4 // 3)

#   " ** "  is 4  power  of  3  
print(4**2)      
# diffrence  of  /  and  //  is that  " / "   is python convert  implicitlly  convert number  to float  
#  using " // "   we  convert   implicite   convertion  of float  to whole number int  
#  PEMDAS  order of  exceution  of  operators
# ()
# **
# * OR /
# /
# +  OR -
# -  

print(3 * 3 + 3 / 3 - 3 )
print(3/3 * 3 + 3 - 3  )

# round function 
#  round(  orginal variable ,length to round up decimal number )

# f strings  at start of string and we  can user  variables in string using print(f"name{name_variable}")

name =  "tarun"  
score = 98
winner  = True

print(f"Candidate Name Is {name} , Score Is {score} and he is {winner} Winnder")