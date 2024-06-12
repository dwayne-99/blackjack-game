import random
import os

def clear_screen():
# ^ Defines a function that clears the console screen

  if os.name == 'nt': # Windows
    os.system('cls')
  else:
    os.system('clear') # Unix-like systems (Linux, macOS)

# ^ The function checks for the os and uses the appropriate clear command using the os import

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# ^ Defines a function that deals a card, 11 is an Ace, 2-9 are numbered cards, 10 is either a Jack, Queen, or King

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# ^ Defines a function that calculates the sum of the cards
# ^ If the score is 21 and there are two cards, the score is 0 to represent a blackjack
# ^ If there is an Ace and the score is over 21, remove the 11 and replace it with a 1

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "You win with a Blackjack! 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win! 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  
# ^ Defines a function that compares the user and computer scores in order to determine the winner

def play_game():
# ^ Defines a function that plays the game

  user_cards = []
  computer_cards = []

# ^ Defines two empty lists to store the user and computer's cards

  is_game_over = False
# ^ Defines a variable that is used to determine if the game is over

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# ^ Deals two cards each to the user and the computer

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

# ^ Game loop: (Calculate the scores, print the current status, check if the game should end, if not ask the user if they want another card)

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

# ^ Computer will hit until it reaches 17 or higher

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

# ^ Prints the final hands and outputs the compare function to determine the winner

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear_screen()
  play_game()

# ^ Main function that plays the game