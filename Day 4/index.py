#  Welcome to Day 4  YOU COMPLETED 3 DAYS CONGRALUTION YUPP  !!!!
# to use random funtions  we need to   // import  random  package  to use random
import random

# random_num = random.randint(1,2)
# print(random_num)

# if random_num  == 1:
#   print("tail")
# else:
#     print("heads")

#  list   to create list  variable_name = [elements of list]
#  understand  methods of  list to  delete or  insert into delete  like append(), 

friends = ["tarun", "dishant" , "chetan"]
print(friends)
friends[-1] = "chetanbha"
print(friends)
friends.append("Jack")
print(friends)
print(f"bill will be pay by {friends[random.randint(0,3)]}")