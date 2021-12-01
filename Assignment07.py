# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Script that showcases the concepts of exception handling and
#   pickling in Python using quotes from the movie "Clueless" and having the
#   user guess who said them
# ChangeLog (Who,When,What):
# JWray,11.27.21,Created Script
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "AppData.dat"  # The name of the data file
file_obj = None  # An object that represents a file
choice_str = ""  # Captures the user number selection
message_str = "" # stores the message returned when checking user input
answer_str = "" # stores answer user provides after reading the quote
quote_row = {} # stores one row from the file
# A list of quotes to be loaded at the start of the script
table_lst = [{'Quote':'Ugh! As if!', 'Who':'Cher'},
             {'Quote':'Hello, that was a stop sign.', 'Who':'Dionne'},
             {'Quote':'Rollin"'" with the homies.", 'Who':'Tai'},
             {'Quote':'I don"'"t wear polyester hair, okay?", 'Who':'Dionne'},
             {'Quote':'Oh, my God, I am totally bugging.', 'Who':'Cher'},
             {'Quote':'If I"'"m to good for him, then how come I"'"m not with him?', 'Who':'Tai'},
             {'Quote':'I had an overwhelming sense of ickiness.', 'Who':'Cher'},
             {'Quote':'Murray, I have asked you repeatedly not to call me woman', 'Who':'Dionne'},
             {'Quote':'And in conclusion, may I please remind you that it does not say "'" RSVP"'" on the '
                      'Statue of Liberty.', 'Who':'Cher'},
             {'Quote':'I"'"m not a prude, I"'"m just highly selective.', 'Who':'Cher'}]

# Processing  --------------------------------------------------------------- #
class Data_Processor:
    """  Performs Processing tasks """

    @staticmethod
    def write_data_to_file(file_name):
        """ Writes data to a binary file

               :param file_name: (string) name of file to write to
               :return: none
               """
        file = open(file_name, 'wb')
        pickle.dump(table_lst, file)
        file.close()
        return

    @staticmethod
    def get_user_quote_from_file(file_name, choice):
        """ Returns quote user choice from file

                       :param: file_name: (string) name of file to read from
                       :param: choice: (int) quote number to return
                       :return: quote_row: (dictionary) quote for user to guess from
                       """

        file = open(file_name, 'rb')

        quotes = pickle.load(file)
        quote_row = {}
        counter = 1

        # loop through the rows to get the one the user chose
        for row in quotes:
            if counter == choice:
                quote_row = row
                break
            else:
                counter = counter + 1
                continue

        return quote_row


# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """  Performs input/output tasks  """

    @staticmethod
    def input_choice():
        """ Gets the quote choice from a user

           :return: string
           """
        choice = str(input('Please enter a number between 1 and 10: ').strip())
        print()  # Add an extra line for looks

        return choice

    @staticmethod
    def check_choice(choice):
        """ Checks to ensure user input a valid choice before processing and raises an exception if not

                :param: choice: (string) input from user
                :return: none
                """
        if choice.isnumeric():
            if int(choice) > 10:
                # message = str(choice) + ' is greater than 10'
                raise Exception(str(choice) + ' is greater than 10')
        else:
            # message = str(choice) + ' is not a number'
            raise Exception(str(choice) + ' is not a number')

    @staticmethod
    def check_answer(row, answer):
        """ Checks if user guess is correct

                :param: row: (dict) row from user choice
                :param: answer: (string) input from user
                :return: message: (bool) tells whether user was right or not
                """
        if row["Who"].lower() == answer.lower():
            message = True
        else:
            message = False

        return message

    @staticmethod
    def try_again():
        """ Checks if user wants to keep playing

               :param: none
               :return: (bool)
               """
        choice = input('Do you want to try again? (y/n): ')

        if choice.lower() == 'y' or choice.lower() == 'n':
            if choice.lower() =='y':
                return True
            else:
                return False
        else:
            raise Exception('please enter a y or n')

# Main Body of Script  ------------------------------------------------------ #

# Load data into the file, uncomment if you need to create/recreate the .dat file
# Data_Processor.write_data_to_file(file_name_str)

# print explanation of game
print('Welcome to  "'"Guess Who Said it"'" using quotes from the movie Clueless\n')

while (True):
    # get user random number input
    choice_str = IO.input_choice()

    try:
        # check if input is valid
        IO.check_choice(choice_str)

        # get the row the user chose
        quote_row = Data_Processor.get_user_quote_from_file(file_name_str, int(choice_str))
        print('Quote: ' + "'" + quote_row["Quote"] + "'")
        answer_str = input("Which character said it? [HINT: It is either Cher, Dionne, or Tai]: ")

        # check if the user answered correctly
        if IO.check_answer(quote_row, answer_str):
            print('You are correct!\n')
        else:
            print('Sorry :( The correct answer was: ' + quote_row["Who"])
            print()

        if IO.try_again():
            continue
        else:
            print('Thanks for playing!')
            break
    except Exception as e:
        print(e)
        print()
        continue



