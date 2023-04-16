import random
from data import data

def start_game():
    def print_game():
        print("##########################  Higher Lower Game #########################")
        print("Welcome to HigherLower Game!")
        print("---------")
        print(f"Compare A: {name_first_item}, a {description_first_item} from {country_first_item}")
        print('----VERSUS!---')
        print(f"Against B: {name_second_item}, a {description_second_item} from {country_second_item}")
        print("---------")
    def print_followers():
        print(f"{name_first_item} has {count_first_item} followers")
        print(f"and {name_second_item} has {count_second_item} followers")

    first_item = random.choice(data)
    second_item = random.choice(data)
    while first_item['name'] == second_item['name']:
        second_item = random.choice(data)

    name_first_item = first_item['name']
    description_first_item = first_item['description']
    country_first_item = first_item['country']
    count_first_item = first_item['follower_count']

    name_second_item = second_item['name']
    description_second_item = second_item['description']
    country_second_item = second_item['country']
    count_second_item = second_item['follower_count']

    print_game()

    user_answer = input("Who has more followers? Type 'A' or 'B':").lower()
    if user_answer == 'a':
        if count_first_item >= count_second_item:
            print("Thats right! you won!")
        elif count_first_item < count_second_item:
            print("Not really, you lose")
        print_followers()
    elif user_answer == 'b':
        if count_first_item <= count_second_item:
            print("Thats right! you won!")
        elif count_first_item > count_second_item:
            print("Not really, you lose")
        print_followers()
    play_again = input("Do you want to play again? Type 'Y' or 'N'").lower()
    if play_again == 'y':
        start_game()
        
start_game()