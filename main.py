# # # Scope and Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies }")

# # # Local Scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()

# print(potion_strength)

# # # Global Scope

# player_health = 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()


# print(player_health)

# # # There is no Block Scope.

# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if game_level < 5:
#         new_enemy = enemies[0]


# print(new_enemy)

# # # Global Constants

# PI = 3.14159
# URL = "https://www.google.com"

# / # / # PROJECT OF DAY 12 # / # / #

def play_game():
    from art import logo
    import random
    from replit import clear

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000!")

    game_over = False
    secret_game_number = random.choice(range(1, 1001))
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 0

    if difficulty == "easy":
        attempts = 16
    else:
        attempts = 8

    while not game_over:
        print(f"You have {attempts} remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == secret_game_number:
            game_over = True
            print(f"Congratulations! You won! The secret number was {guess}!\nYou had {attempts} attempts left!\n")
        elif guess > secret_game_number:
            attempts -= 1
            if attempts >= 1:
                print(f"{guess} is too high!\nGuess again!\n")
        elif guess < secret_game_number:
            attempts -= 1
            if attempts >= 1:
                print(f"{guess} is too low!\nGuess again!\n")

        if attempts == 0:
            game_over = True
            print(f"Game over! The secret number was {secret_game_number}!")

        if game_over:
            play_again = input("Dou you want to play again? Type 'y' or 'n': ")
            if play_again == "y":
                clear()
                play_game()
            else:
                print("Goodbye! 8D")


play_game()
