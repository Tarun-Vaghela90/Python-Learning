# started  day  3  
#  if else  statement and  oerators

if  45 > 5:
    print("it is greater than 5")
else:
    print("it is not greater then 5")
# comparition  operators  are  == , >= ,<= ,  ===


# modulo  %
print(10/3)
print(10%3)

# exercise   
#  find odd  or even number

num =  int(input("Enter The Number"))

if(num%2 == 0):
    print(f"{num} is  even")
else:
    print(f"{num} is  odd")
    
#  nested  if else  statements
#  using  if/ elif / else

if 12 >= 0:
    print("12 is greate rthen zero nested if else example")
    if(0 == 0):
        print("0 equa;l to 0")
else:
    print(f"{num} is  odd")

#excerice  prizzz   ask  size , want pepraoni ,  cheesse   ,  set  prize  ,   gie total  bill
 
print("Welcome to Pizza Store ")

# Get inputs from the user
pizza_size = input("What size of pizza do you want? S, M, or L: ").lower()
pepperoni_want = input("Do you want to add pepperoni? y or n: ").lower()
cheese_want = input("Do you want to add cheese? y or n: ").lower()

# Set base prices for different pizza sizes
s = 150
m = 180
l = 230

# Set prices for additional toppings
pepperoni = 20
cheese = 25

# Initialize total bill
total_bill = 0

# Add the price of the pizza based on size
if pizza_size == "s":
    total_bill += s
elif pizza_size == "m":
    total_bill += m
elif pizza_size == "l":
    total_bill += l

# Add price for pepperoni if the user wants it
if pepperoni_want == "y":
    total_bill += pepperoni

# Add price for cheese if the user wants it
if cheese_want == "y":
    total_bill += cheese

# Print the total bill
print(f"Your total pizza bill is: {total_bill}")


# operators