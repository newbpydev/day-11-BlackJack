# ############ Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random
from art import logo
from art import image_card
# from replit import clear
import os


# clear = lambda:
def clear():
    os.system('cls')


# clear()


############## Functions Playground ###############

def deck_builder():
    """Used to build a deck of card total 52 without Joker"""
    # is_there_a_joker = False
    card_types = ["Spade", "Heart", "Diamond", "Club"]
    # card_type_image = image_card
    card_names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                  "King"]
    card_points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    complete_deck = []

    count = 0
    for type_name in card_types:
        for card in range(len(card_names)):
            complete_deck.append(
                {"type": type_name, "name": card_names[card], "points": card_points[card], "image": image_card[count],
                 "img_id": count})
        count += 1
    return complete_deck


# -------------------------------------------------
def select_and_remove_a_card(deck_of_cards):
    # select a card from the card deck
    card_selected = random.choice(deck_of_cards)
    deck_of_cards.remove(card_selected)
    return card_selected


# ------------------------------------------------
def calculate_card_points(choice_list):
    points_total = 0
    ace_counter = 0
    should_continue = True
    for point in choice_list:
        points_total += point["points"]
        if "Ace" in point['name']:
            ace_counter += 1

    if points_total > 21 and ace_counter != 0:
        ace_count_inside = 0
        while should_continue:
            if points_total > 21 and ace_count_inside != ace_counter:
                points_total -= 10
                ace_count_inside += 1
            else:
                should_continue = False

    return points_total


# testing
# -------------------------------------------------
def display_cards_at_hand(deck_of_cards, is_player, reveal_all=False):
    # is_player = False
    # reveal_all = False
    output = ""
    if not is_player:
        output = f"The computer has a {deck_of_cards[0]['name']} of {deck_of_cards[0]['type']} with a point of {deck_of_cards[0]['points']}."
        if reveal_all:
            for card in range(1, len(deck_of_cards)):
                output += f"\nIt has a {deck_of_cards[card]['name']} of {deck_of_cards[card]['type']} with a point of {deck_of_cards[card]['points']}."
        print(output)
    else:
        for info in deck_of_cards:
            # print(info["type"])
            output = f"You have a {info['name']} of {info['type']} with a point of {info['points']}."
            print(output)


# -------------------------------------------------
def reveal_final_score(player_choice, computer_choice):
    p1_score = calculate_card_points(player_choice)
    p2_score = calculate_card_points(computer_choice)

    if p1_score > 21:
        print(f"\n(╥﹏╥) You lose, it's a bust. You had {p1_score}, the computer had {p2_score} points.\n")
    elif p1_score == 21:
        print(f"\n(⌐■_■) You win. You had a Blackjack\n")
    elif (p1_score < p2_score and p2_score > 21) or p1_score > p2_score:
        print(f"\n(⌐⊙_⊙) You win. You had {p1_score}, the computer had {p2_score} points.\n")
    elif p1_score == p2_score:
        print(f"\n(｡◕‿‿◕｡) It's a draw.You had {p1_score}, the computer had {p2_score} points.\n")

    else:
        print(f"\n(╥﹏╥) You lose, You had {p1_score}, the computer had {p2_score} points.\n")


# -------------------------------------------------
def display_cards_images_at_hand(deck_of_cards, is_rest_hidden=False):
    num_of_lines = 6
    card_num = ""
    img_complete = []

    for each_card in deck_of_cards:
        card_sym = each_card['image']
        if each_card['points'] >= 2 and each_card["points"] <= 9:
            card_num = " " + str(each_card['points'])
        elif each_card['points'] == 11:
            card_num = " A"
        elif each_card['points'] == 10:
            if each_card['name'] == "Ten":
                card_num = "10"
            elif each_card['name'] == "Jack":
                card_num = " J"
            elif each_card['name'] == "Queen":
                card_num = " Q"
            elif each_card['name'] == "King":
                card_num = " K"
        # img_id = each_card["img_id"]
        for line in range(num_of_lines):
            image = [
                f"     _____ ",
                f"    |{card_num + card_sym}  |",
                f"    |     |",
                f"    |  {card_sym}  |",
                f"    |     |",
                f"    |__{card_num + card_sym}|",
                # f"           ",
            ]
            img_complete.append(image[line])

    # end_of_cards = False
    disp_cards_complete = ""
    pos = 0

    # If is hidden, ex: the computer's starting hand
    if is_rest_hidden == True:
        num_of_cards = 1
        counter = 0
        for line in range(num_of_lines):
            pos = counter
            for item in range(num_of_cards):
                disp_cards_complete = disp_cards_complete + img_complete[pos]

                if item == num_of_cards - 1:
                    pos = 0
                    disp_cards_complete += "\n"
                else:
                    pos += 6
            counter += 1
        print(disp_cards_complete)
    else:
        # while not end_of_cards:
        num_of_cards = round(len(img_complete) / 6)
        counter = 0
        for line in range(num_of_lines):
            pos = counter
            for item in range(num_of_cards):
                disp_cards_complete = disp_cards_complete + img_complete[pos]

                if item == num_of_cards - 1:
                    pos = 0
                    disp_cards_complete += "\n"
                else:
                    pos += 6
            counter += 1
        print(disp_cards_complete)

        # end_of_cards = True


# -------------------------------------------------
def display_combo_1_hid(computer_choice, user_choice):
    display_cards_at_hand(computer_choice, False)
    # Displays images of the cards at hand
    display_cards_images_at_hand(computer_choice, True)
    display_cards_images_at_hand(user_choice)
    display_cards_at_hand(user_choice, True)


def display_combo_show_all(computer_choice, user_choice):
    display_cards_at_hand(computer_choice, False)
    # Displays images of the cards at hand
    display_cards_images_at_hand(computer_choice, False)
    display_cards_images_at_hand(user_choice)
    display_cards_at_hand(user_choice, True)


#################Code Starts Here##########

# should_continue = True

def blackjack_game():
    clear()
    computer_choice = []
    user_choice = []
    hit_me = True
    total_points_user = 0
    total_points_computer = 0

    # 2 Starting cards for me and the computer
    computer_choice.append(select_and_remove_a_card(cards_deck))
    computer_choice.append(select_and_remove_a_card(cards_deck))
    user_choice.append(select_and_remove_a_card(cards_deck))
    user_choice.append(select_and_remove_a_card(cards_deck))

    # Calculate the total of points accumulated
    total_points_computer += calculate_card_points(computer_choice)
    total_points_user += calculate_card_points(user_choice)

    while total_points_computer < 17:
        total_points_computer = 0
        computer_choice.append(select_and_remove_a_card(cards_deck))
        total_points_computer += calculate_card_points(computer_choice)

    display_combo_1_hid(computer_choice, user_choice)

    ##########################################################
    # for card in computer_choice:
    #     if "Ace" in card['name']:
    #         print("Found an Ace in Computer_choice")
    # for card in user_choice:
    #     if "Ace" in card['name']:
    #         print("Found an Ace in user_choice")
    # testing = "Ace" in cards_deck
    # print(testing)
    #######################################

    while hit_me:
        hit_me_answer = input("Do you want another card? Type 'y' for yes or 'n' for no: ")

        if hit_me_answer == ("y" or "Y"):
            clear()
            user_choice.append(select_and_remove_a_card(cards_deck))
            display_combo_1_hid(computer_choice, user_choice)
            if calculate_card_points(user_choice) > 21:
                clear()
                display_combo_show_all(computer_choice, user_choice)
                reveal_final_score(user_choice, computer_choice)
                hit_me = False
                # should_continue = False
        elif hit_me_answer == ("n" or "N"):
            clear()
            display_combo_show_all(computer_choice, user_choice)
            reveal_final_score(user_choice, computer_choice)
            # should_continue = False
            hit_me = False

    play_again = input("Do you want to continue playing Blackjack? type 'y' to continue, or 'n' to quit game: ")

    if play_again == 'y':
        blackjack_game()
    else:
        clear()
        print("Thank you for playing!")
        return


clear()
print(logo)
play = input("Do you want to play Blackjack? Type 'y' to play, or 'n' to exit: ")

if play == ('y' or 'Y'):
    cards_deck = deck_builder()
    blackjack_game()
else:
    print("Thank you, come again!")
    # reveal_final_score(user_choice, computer_choice)

    # answer = input("Do you want to select another card? type 'y' to continue or type 'n' to stop playing: ")
    # if answer == "n":
    #     should_continue = False

################ Scrap Code #####################


##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
