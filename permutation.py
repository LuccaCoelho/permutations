# Viniccius Lucca FLorindo Coelho
# CS-1410
# 09/15/2023

'''
   This is code 1 is design to get and accept an input from user. The input is then 
   validaded to meet the criterias. Once the input is validaded, it will then output
   every possible permutation of the user input, organizing from first to last letter.
'''

# Import specific module used in this program. Easiest way to create permutations.
from itertools import permutations

# importing module search, needed to check if there are special letters or whitespace on user input.
from re import search

# function will check user_input for errors.


def check(get_input):
    '''get_input is the user input. We make the input go through a series of checks,
       if the check identifies an error, and if it identify it will raise the error '''

    # Try statement to check for value errors
    # checks if user input has any digits.
    if any(character.isdigit() for character in get_input):
        raise ValueError("Can't use numbers. Try again.")

    # checks if user didn't write anything as a input.
    if get_input == '':
        raise ValueError('Nothing computated. Try again.')

    # checks if there are any special character or whitespaces in user input.
    if search('[^a-zA-Z]', get_input) is not None:
        raise ValueError('Your word contains special character(s) or whitespace(s). Try again.')

    # checks if user repeated any letters.
    if len(set(get_input)) != len(get_input):
        raise ValueError("Can't repeat letters. Try again.")

# Function will create a list of permutation ready to print.


def gen_perm(perm):
    '''Perm is a random variable at the moment, but it will later be switched 
       for the user input. We create an empty list, and add the desired 
       permutations to it. we will separate the letters before and after the 
       index and create permutations with them, then add the index to the beggining
       of the permutations.'''

    # empty list.
    perm_list = []

    # This for loop will create all possible permutations out of the user input in the right order.
    for i, begin in enumerate(perm):
        # begin is setting our index value to be in the user input,
        # then will exclude the index value and create permutations
        # with every remaining letters.
        begin = perm[i]
        rest_char = perm[:i] + perm[i+1:]
        rest_perm = permutations(rest_char)

        # this loop will organize the permutations to have all permutations with the first
        # letter in front appear first, then the second appear second, etc. until the last
        # letter of the input.
        for char in rest_perm:
            # put the index value first and add the permutations of the remaining
            # characters and add it to the empty list.
            perm_word = begin + ''.join(char)
            perm_list.append(perm_word)

    return ' '.join(perm_list)

# Our main function that will put everything together and (hopefully) output exactly what we want.


def main():
    '''This main function will let user know they can stop, and ask them for a word.
    Once they write the word, it will run the "error checker" function and if everything is good,
    it will create the permutations, and print everything organized'''

    # While loop will make sure to always keep asking user for new words until they ask to stop.
    while True:
        # this will be our user input. lower() to make the string lower case, and casefold() to
        # erase any extra spaces in the beggining or end of the user input
        print('You can always stop. Just say the magic word')
        get_input = input('Enter a word: ').lower().strip()

        # If statement to break the loop if user types the "magic word".
        if get_input == 'abrakadabra' or get_input == 'abracadabra':
            print('You are no fun :(')
            break

        # try stetement to check for errors
        try:
            # call the check function
            check(get_input)

            # Run function that created the permutations and print the permutations
            perm_create = gen_perm(get_input)
            print(f'All permutations of word "{get_input.upper()}" are:')
            print(perm_create)
        # if any value error was raised it will print it
        except ValueError as error:
            print(f"{error}")


if __name__ == '__main__':
    main()


# Thoughts

# This program was actually fun to create. I spent some time researching
# the best way to create and use permutations and the best way to error
# check it. I ended up using both modules, permutations and search,
# simply because I wanted a complete code that would give me the output
# that I wanted, and to check all the errors that I wanted. I researched many
# different ways to check for specific things in string, like check for numbers,
# or special characters, etc. I had a couple of parts that challenged me,
# like creating the function that generated all permutations and organize them,
# but it was nice to search through the permutation module in the python website,
# as well as, geek for geek and w3 python website. I'm not sure if the way I code
# is ugly, pretty, good, bad, so I hope I did a good code here. My creative element
# is I have a "magic word" for the user to stop the code
