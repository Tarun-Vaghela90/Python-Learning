# bill  total
# tip  how much in percentage 10  12 or  15
# how many people will be  spliting
# how much each person should be pay


bill_total = float(input("Enter Total Bill  Amount\n"))
tip  = int(input("How much Tip you  Would LIke to Give 10 , 12 or 15\n"))
people = int(input("How Many Person to split\n"))

tip_cal  = tip/100
bill_cost_with_tip = tip_cal * bill_total
bill_final  =   bill_cost_with_tip + bill_total 
bill_per_person = bill_final / people
final = round(bill_per_person, 2)
print ("each person should tip is :"+ str(bill_cost_with_tip ))
print (f"each person should pay:${final} ")