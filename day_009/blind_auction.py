print("Welcome to the secret auction program")
bids = {}
bidding_finished = False

def add_bid(name, bid):
    bids[name] = bid

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name_of_bidder = input("What is your name?: ")
    bid_of_bidder = int(input("What is your bid?: $"))
    add_bid(name_of_bidder, bid_of_bidder)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
