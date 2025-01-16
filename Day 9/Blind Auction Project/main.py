# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def user_information(bidders):

    name = input("What is your name ? : \n ")
    amount = input("Bid amount in ZAR : \n ")
    bidders[name] = amount
    return input("Are you the last person ? : ")


def winner(my_dict):
    return max(my_dict.values())



my_bidders = {}
more_people = user_information(my_bidders)

while more_people.lower() != "yes":
    print("\n"*100)
    more_people = user_information(my_bidders)
else:
    print("The highest bidder is : R" + winner(
        my_bidders
    ))






