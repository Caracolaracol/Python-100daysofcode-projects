
# you can call clear() to clear the output in the console

from day10.art import logo


at_loop = True
list_bids = []
is_firstuserbid = True
first_userbid = 0
highest_bid = 0
while at_loop:
    print(f"\n{logo}")
    name_asked = input("What its your name?")
    bid_price = int(input("Input your bid price"))

    bid_user = {
        "name": name_asked,
        "bid": bid_price
    }
    list_bids.append(bid_user)


    keep_asking = input("Are there any other users who want to bid?").lower()
    if keep_asking == 'yes':
        at_loop = True
    elif keep_asking == 'no':
        
        print(f"\n{logo}")
        for user in list_bids:
            if is_firstuserbid:
                is_firstuserbid = False
                highest_bid = user["bid"]
  
            if highest_bid < user["bid"]:
                highest_bid = user["bid"]        
        at_loop = False

print(F"The winner is who bet ${highest_bid}")