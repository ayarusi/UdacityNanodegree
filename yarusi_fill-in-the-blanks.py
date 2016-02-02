
# A list of game levels to be chosen by the user and passed in to the play the game function - WORKS
game_level = ["easy", "medium", "hard"]

# A list of acceptable answers to be passed into the play game function. 
answer_list = ["function","values","none","list"]


# Print the game introduction on the screen - WORKS
user_input_intro = raw_input("Please select a game difficulty level, by typing in either 'easy', 'medium', or 'hard':")

# Check if user chosen level is in 'easy', 'medium', or 'hard'. If a valid selection, print the user chosen level
# on the screen. If not, give error message and prompt to restart the game. - WORKS
if user_input_intro in ('easy', 'medium', 'hard'):
    print ("You've chosen the " + user_input_intro +" game!")
else:
    print ("Invalid input. Please restart the game and try again!")
    quit()                        
print

# A number of guesses to be chosen by the user and pass in to the play the game function - WORKS
user_input_no_guesses = raw_input("How many guesses would you like for this problem? Please enter a positive whole number:")
print
#for testing
#print user_input_guesses

# The following returns the appropriate text string that correspond to the game level chosen by the user - WORKS
if user_input_intro == 'easy':
    game_string = "This is the easy game. A __1__ is created with the def keyword. You specify the inputs a function takes by adding __2__ separated by commas between the parenthesis. __1__s by default return __3__ if you don't specify the value to return. __2__ can be standard data types such as string, number, dictionary, tuple and __4__, or can be more complicated such as objects and lambda functions."
if user_input_intro == 'medium':
    game_string = "This is the medium game."
if user_input_intro == 'hard':
    user_input_intro = "This is the hard game."
print game_string
print

# Prompt user to answer question
current_guess = 1
user_input_answer = raw_input("What should be sustituted for answer " + str(current_guess) + "?")
current_guess = current_guess + 1

# Check if next blank number is equal to or less than the number of blanks chosen by the user



        
#def next_guess(user_input_no_guesses):
#   if current_guess <= user_input_no_guesses:
# The following prompts the user to enter the answer to the question
#       return user_input_answer == raw_input("What should be sustituted for answer " + current_guess + "?")
#   else:
#       return ("You did it!")


# Checks if the word input by the user is in the answer_list string.
def word_in_al(user_input_answer, answer_list):
    for pos in answer_list:
        if pos in user_input_answer:
            return pos
    return NONE


# Plays the game depending on the level chosen. A player is prompted to replace the numbered blanks in game_string
# which appear in parts_of_speech with their own words.
def play_game(game_string, user_input_no_guesses, user_input_answer):
    replaced = []
    game_string = game_string.split() # Split the game string into a list
    current_guess = 1
    while current_guess <= user_input_no_guesses: # Ensure the current guess is not a larger number than the user inputed
        #Prompt user to answer question
        user_input_answer = raw_input("What should be sustituted for answer " + str(current_guess) + "?") 
        current_guess = current_guess + 1

    #Check for answers in answer list and replace if correct
    for user_input_answer in answer_list: 
        replacement = word_in_al(user_input_answer,answer_list)
        if replacement != None:
            word = word.replace(replacement,user_input_answer)
            replaced.append(word)
        else:
            replaced.append(word)
        replaced = " ".join(replaced)
        return replaced
    print replaced
                                
      

# User a for loop to replace numbered blanks with user correct answers

#1 game_string[6, 29]
#2 game_string22,42
#3 game_string[33]

