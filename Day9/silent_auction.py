auction_bidders = {}
auction_under_way = True
highest_bid = 0

while auction_under_way:
    bidder_name = input("What is your name? ")
    bid = float(input("What's your bid? "))

    auction_bidders[bidder_name] = bid

    print("Are there any other bidders? Type 'yes' or 'no'.")
    other_bidders = input("")
   
    if other_bidders == "no":
        print("Auction ended")
        auction_under_way = False
    elif not other_bidders == 'yes': 
        print("Your bid is invalid due to your answer to the previous question. Please try again.")

for bidder in auction_bidders:
    if auction_bidders[bidder] > highest_bid:
        highest_bid = auction_bidders[bidder]

highest_bidder = list(auction_bidders.keys())[list(auction_bidders.values()).index(highest_bid)]

print(f"The winner is {highest_bidder} with a bid of ${"{:.2f}".format(highest_bid)}.")