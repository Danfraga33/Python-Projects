from replit import clear
from art import logo

playing = True

while playing:
    print(logo)
    name = input("What is your name? \n")
    bid = input("How much would you like to bid? \n")
    bid_dict = {}

    bid_dict[name] = bid

    again_q = input(
        "Is there another bidder? Type yes for yes or no for no\n")
    if again_q == 'yes':
        clear()
    elif again_q == 'no':
        print(
            f'The winner is {max(bid_dict)} with a bid of {max(bid_dict.values())}'
        )
        playing = False
