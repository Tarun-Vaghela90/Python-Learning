#  auction  project
import art
car_auction={
    "cars":["BMW","Audi","Rolls Royal"],
    "bidders":[]
}
print(art.logo)
print(art.greeting_logo)

def highest_bidder(car_bidders,car_number):
    length_bid = len(car_bidders["bidders"])
    high_bidder_name = ''
    highest_bid =0
    print(car_bidders)    
    # finding  Highest Bidding Amount
    for bid in range(length_bid):
        if car_bidders["bidders"][bid][1] > highest_bid:
            highest_bid=car_bidders["bidders"][bid][1]
            high_bidder_name =car_bidders["bidders"][bid][0]
    print(f'Highsest  Bid For {car_bidders["cars"][car_number]} Made By {high_bidder_name} With  Bidding Amount Is {highest_bid}')
    print("\n"*10)



car_count=0
print("First Car Is "+ car_auction["cars"][car_count] )

bidding_done = True
while(bidding_done):
    name_bidder = input("Enter Name Of Bidder ?\n")
    bidder_amount = int(input("Enter Your Bid ?\n"))
    car_auction["bidders"]+= [[name_bidder,bidder_amount]]
    more_bidders = input("Is Anyone want to Bid ? Type Yes else No\n").lower()
    print("\n"*100)
    
    if more_bidders == "no":
        highest_bidder(car_bidders=car_auction,car_number=car_count)
        next_bid = input("Do Want To Bid On Other Cars ? Type 'Yes' Else 'No' ").lower()
        if next_bid == 'no':
            highest_bidder(car_bidders=car_auction,car_number=car_count)
            bidding_done=False
            print("\n"*20)
        elif next_bid == 'yes':
            car_count+=1
            car_auction["bidders"]=[] # empty bidder for new  car
            print("Next Car Is "+ car_auction["cars"][car_count] )


   

