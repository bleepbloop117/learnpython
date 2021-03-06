import random

game_length = 4
prompt = "Guess a number between 1 and 10!"

def game():
  while True:
    play_again = input("Y/N > ")
    if play_again == "y" or play_again == "Y":
      game_length = 4
      print(prompt)
      break
    elif play_again == "n" or play_again == "N":
      exit()
    else:
      print("I'm sorry. That's not a recognized command.")

print("Nick's super awesome number guessing game.")
print("What is your name?")
user_name = input("> ")

print("Nice to meet you {}. Let's get started.".format(user_name))
print(prompt)

while game_length > 0:
  ai_guess = random.randint(1,10)

  user_guess = input("> ")
  user_guess = int(user_guess)

  if ai_guess == user_guess:
      print("{} you won! Play again?".format(user_name))
      game()

  elif ai_guess != user_guess:
    game_length = game_length-1
    print("Oops wrong guess! You have {} more guesses.".format(game_length))

    if game_length == 0:
      print("I'm sorry {} but you've lost. Would you like to play again?".format(user_name))
      game()
