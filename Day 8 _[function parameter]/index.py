# create and call  function

# def  greet():
#     print("Hello !")
#     print("My Name Is James")
#     print("I Am Your Helper and Guide Into Learning Python")
# greet()

#  function that allow inputs

# def greet_with_name(name):
#     print(f'Hello ! {name}')
#     print("My Name Is James")
#     print("I Am Your Helper and Guide Into Learning Python")

# greet_with_name(123)

#  name = 123   //  name is  paramter and  123  is  argument


#  function with two parameter

# def greet_with(name, location):
#     print(f'Hello ! I Am {name}')
#     print(f'I Am From {location}')
# greet_with("Tarun", "India")
# # position argument  exmaple
# greet_with("London", "Dishant" )

# code  exrcise

def calculate_love_score(name1, name2):
    check_TRUE = "TRUE"
    check_Love = "LOVE"
    count_love = 0
    name = name1 + name2
    count_true = 0
    count_love = 0
    for letter in name:
        if letter in check_TRUE.lower():
            count_true+= 1
        if letter in check_Love.lower():
             count_love+=1   
    total_count = f'{count_true}' + f'{count_love}'
    print(int(total_count))   
calculate_love_score("tarun","monica")