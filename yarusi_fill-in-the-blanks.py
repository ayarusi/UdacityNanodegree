# A list of game levels to be chosen by the user and passed in to the play the game function - WORKS
game_level = ["easy", "medium", "hard"]

# A list of acceptable answers to be passed into the play game function. 
answer_list = ["function","values","none","list","world","python","print",]

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

# The following returns the appropriate text string that correspond to the game level chosen by the user - WORKS
if user_input_intro == 'easy':
    game_string = "This is the easy game. A __1__ is created with the def keyword. You specify the inputs a function takes by adding __2__ separated by commas between the parenthesis. __1__s by default return __3__ if you don't specify the value to return. __2__ can be standard data types such as string, number, dictionary, tuple and __4__, or can be more complicated such as objects and lambda functions."
if user_input_intro == 'medium':
    game_string = "This is the medium game. Hello __1__! In __2__ this is particularly easy; all you have to do is type in: __3__ 'Hello __1__!' Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser, but it's a step in learning __2__ syntax, and that's really its purpose."
if user_input_intro == 'hard':
    game_string = "This is the hard game. When you create a __1__, certain __2__s are automatically generated for you if you don't make them manually. These contain multiple underscores before and after the word defining them. When you write a __1__, you almost always include at least the __3__ __2__, defining variables for when __4__s of the __1__ get made. Additionally, you generally want to create a __5__ __2__, which will allow a string representation of the method to be viewed by other developers. You can also create binary operators, like __6__ and __7__, which allow + and - to be used by __4__s of the __1__. Similarly, __8__, __9__, and __10_ allow __4__s of the __1__ to be compared <with <,>, and ==>."
print game_string
print

current_guess = 1
user_input_answer = raw_input("What should be sustituted for answer " + str(current_guess) + "?") # Prompt user to answer question

# Checks if the word input by the user is in the answer_list string.
def word_in_al(user_input_answer, answer_list):

    while current_guess <= user_input_no_guesses: #Ensure the current guess is not a larger number than the user inputed amount
        if user_input_answer in answer_list:
                print game_string
        else:
                print 'Incorrect answer, please guess again.'
	    #user_input_answer = raw_input("Incorrect guess. Please try again.") # Prompt user to answer question
	    #next_guess(user_input_no_guesses, current_guess)
            #current_guess = current_guess + 1
	


# Plays the game depending on the level chosen. A player is prompted to replace the numbered blanks in game_string which appear in parts_of_speech with their own words.


def play_game(game_string, user_input_answer):
    replaced = []
    game_string = game_string.split() # Split the game string into a list

    for user_input_answer in answer_list: #Check for answers in answer list and replace if correct
        replacement = word_in_al(user_input_answer,answer_list)
        if replacement != None:
            word = word.replace(replacement,user_input_answer)
            replaced.append(word)
        else:
            replaced.append(word)
        replaced = " ".join(replaced)
        return replaced
    
#print play_game(game_string, user_input_answer)
                                
      


