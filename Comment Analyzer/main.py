"""
******************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Harley Thorpe
Student ID: 251408871, hthorpe4
File created: November 13, 2024
******************************
This program asks the user to enter a keyword .tsv file,
a comment .csv file, a country, and a .txt report filename.
From this data, the program sifts through the comment .csv
file and identifies any keywords from the keyword .tsv file,
classifying the comment's emotions. It then results the
total emotions of the comments from the indicated country
from the user.
"""

import os.path
from emotions import *

VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']


def ask_user_for_input():

    # Get keyword file input from user
    keyword_file = input("Input keyword file (ending in .tsv):")

    # Raise ValueError if .tsv is not in file
    # Raise IOError if file does not exist
    if ".tsv" not in keyword_file:
        raise ValueError("Keyword file does not end in .tsv!")
    if not os.path.exists(keyword_file):
        raise IOError(f"{keyword_file} does not exist!")

    # Get comment file input from user
    comment_file = input("Input comment file (ending in .csv):")

    # Raise ValueError if .csv is in comment file
    # Raise IOError if file does not exist
    if ".csv" not in comment_file:
        raise ValueError("Comments file does not end in .csv!")
    if not os.path.exists(comment_file):
        raise IOError(f"{comment_file} does not exist!")

    # Get country input from user
    country = (input('Enter a country to analyze (or "all" for all countries):')).lower().strip()
    # If they did not put a valid country or all, raise an error
    if country not in VALID_COUNTRIES and country != "all":
        raise ValueError(f"the text {country} is not a valid country to filter by!")

    # Get report file input from user
    report_file = input("Enter the name of the report file (ending in .txt):")

    # If they didn't put .txt in the file, raise a ValueError
    # If the file already exists, raise an IOError
    if ".txt" not in report_file:
        raise ValueError("Report file does not end in .txt!")
    if os.path.exists(report_file):
        raise IOError(f"{report_file} already exists!")

    # Return all the inputs in a tuple
    return keyword_file, comment_file, country, report_file


def main():

    # Loops until all the inputs are valid
    while True:
        # Keep on asking for the user for input until no errors occur
        try:
            data = ask_user_for_input()
            break
        except ValueError as e:
            print(e)
        except IOError as e:
            print(e)

    # Set up the comment list, key word dictionary, and report filename
    comment_list = make_comments_list(data[2], data[1])
    keywords = make_keyword_dict(data[0])
    report_filename = data[3]

    # Output the most common emotion to the user
    try:
        print("Most common emotion is:", make_report(comment_list, keywords, report_filename))
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
