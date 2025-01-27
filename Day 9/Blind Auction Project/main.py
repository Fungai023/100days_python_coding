import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

def user_information(bidders):
    name = username()
    amount = bid_amount()
    bidders[name] = amount

def username():
    name = input("What is your name ? : \n ")
    while not name.isalpha() or len(name)==0 :
        print("Invalid name , please try again","red" )
        name = input("What is your name ? : \n ")
    return  name

def bid_amount():
    amount = int(input("Bid amount in ZAR : \n "))
    while not type(amount)!= int and len(str(amount)) == 0 :
        print("Invalid bid amount, please try again .")
        amount = int(input("Bid amount in ZAR : \n "))
    return amount


def is_last_person():
    is_last = input("Are you the last person ?(yes/no) : ")
    while is_last.lower() not in ["yes", "no"]:
        print(f'{is_last} is not valid . Please enter valid input.')
        is_last = input("Are you the last person ? : ")
    return is_last


# TODO-4: Compare bids in dictionary
def winner(my_dict):
    return max(my_dict.values())

def main():
    my_bidders = {}
    print(art.logo)
    user_information(my_bidders)
    more_people = (is_last_person())
    while more_people.lower() != "yes":
        print("\n"*90)
        user_information(my_bidders)
        more_people = is_last_person()
    else:
        win = winner(my_bidders)
        print(f'The highest bidder is {[x for x,y in my_bidders.items() if y == win][0]} : R {win}')
        print("Item successfully sold .")

if __name__ == "__main__":
    main()

