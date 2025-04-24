#   we  learn  about  dictionaries  &  nesting on Day 9
#  dictionary


# person = {
#     "name":"Tarun",
#     "Eduacation" : "B.Tec (Computer Engineering)"
# }
# name =  key  and  "tarun" = Value
# key name must be  currect
# print(person["name"])
# add another feild in person dynamic
# person["skills"] = "Javascript, React , Express.js , Node.js , MongoDB , BootStrap , Taiwind CSS , Python , Html , Css , SQL"
# print(person)

#  creating  empty  dictionary

# empty_dictionary = {}

#  clearing  exiting dictionary

# person={}
# print(person)

#  edit an item  in   a  dictionary

# person["name"] = "Chetan"
# print(person)

# loop  throught  dictionary
# for key in person:
# using  loop   its give key of dictionary
    # print(key)
    # print(person[key])

#  exrcise

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}
# for  key in student_scores:
#     print(student_scores[key])
    
#     if student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)

#  how to access  item in this
# travel_log ={
#     "france": ["Paris", "Lille", "dijon"],
#     "germany": ["berlin", "stuttgart"]
# }
# print(travel_log["france"][1])  # its print lille

# using loop
# for city in travel_log["france"]:
#     print(city)

# nested_list=["a", "b",["c","d"]]
# print(nested_list[2][1])

# nested  dictionaries
travel_log ={
    "france":{
        "city_visited":["Paris", "Lille", "dijon"],
        "total_visited":1
    },
    "germany": {
        "city_visited":["berlin", "stuttgart"],
        "total_visited":1
    }
}

#  to access  nested dictionary  first  dic name followed  by ["key name"]["nested keyname"][if nested list then give index number / name]
print(travel_log["germany"]["city_visited"][1])  