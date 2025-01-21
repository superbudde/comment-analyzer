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

EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']


def clean_text(comment):

    # Make the comment lower case
    comment = comment.lower()

    '''Loop through the characters of the comment. If
    the character is not in the alphabet from a-z (or A-Z),
    replace all of them with spaces.'''
    for i in range(len(comment)):
        if not comment[i].isalpha():
            comment = comment.replace(comment[i], " ")

    # Return result
    return comment


def make_keyword_dict(keyword_file_name):

    # Dictionary full of words and their associated emotions
    # This dict will be the final result returned
    keywords = {}

    # Open file that user inputted when calling function
    f = open(keyword_file_name, 'r')

    # Loop through tsv file
    line = f.readline()
    while line != "":
        # Make a list of all values separated by tab
        line_list = line.split("\t")
        # Make a dictionary of the word in the file
        keywords[line_list[0]] = {}

        # Loop through the line, if any value is one,
        # set the emotion value to 1. If not, set it
        # to 0.
        for i in range(1, len(line_list)):
            keywords[line_list[0]][EMOTIONS[i-1]] = int(line_list[i].strip())

        line = f.readline()

    # Close file and return result
    f.close()
    return keywords


def classify_comment_emotion(comment, keywords):

    # Clean the comment of punctuation and capitals
    comment = clean_text(comment)
    # Make comment a list of words split by comments
    comment = comment.split(" ")

    # The dictionary for the total emotions found in comment
    emotions = {
        "anger": 0,
        "joy": 0,
        "fear": 0,
        "trust": 0,
        "sadness": 0,
        "anticipation": 0
    }

    # Loop in the comment, and look for words that are associated with emotions.
    # If so, increment it on the emotions dict.
    for word in comment:
        if word.strip() in keywords:
            for emotion in keywords[word.strip()]:
                if keywords[word][emotion] != 0:
                    emotions[emotion] += 1
    # Loop through the emotions dict to find the highest value and return it
    for emotion in emotions:
        highest = True
        for value in emotions:
            if emotions[emotion] < emotions[value]:
                highest = False
        if not highest:
            continue
        return emotion

    return None


def make_comments_list(filter_country, comments_file_name):

    # The list of comments that will be returned
    comment_list = []

    # Open the file the user put in the function call
    f = open(comments_file_name, 'r')

    # Loop through the file
    line = f.readline()
    while line != "":
        # Split the file into a list of values separated by commas
        line_list = line.split(",")

        # If the country of the line is the same as the one the user inputted,
        # or the user put "all", add a dictionary of the comment in the list
        if line_list[2] == filter_country or filter_country == "all":
            comment_dictionary = {"comment_id": int(line_list[0]), "username": line_list[1], "country": line_list[2],
                                  "text": line_list[3].strip()}
            comment_list.append(comment_dictionary)

        line = f.readline()

    # Close file and return result
    f.close()
    return comment_list


def make_report(comment_list, keywords, report_filename):

    # Create the report file
    f = open(report_filename, 'w')

    # Dictionary that will count all the comment's emotions
    emotions = {
        "anger": 0,
        "joy": 0,
        "fear": 0,
        "trust": 0,
        "sadness": 0,
        "anticipation": 0
    }

    # Raise error if no comments found
    if len(comment_list) == 0:
        raise RuntimeError("No comments in dataset!")

    # Increment the emotions in the emotions dictionary correlating with
    # The comment's emotions
    for comment in comment_list:
        emotion = classify_comment_emotion(comment['text'], keywords)
        emotions[emotion] += 1

    # Find the highest emotion
    highest_emotion = max(emotions, key=lambda e: emotions[e])

    # Write down the most common emotion in the file
    f.write("Most common emotion: " + highest_emotion + "\n\n")

    # Write down all the emotion totals in the file
    f.write("Emotion Totals\n")
    for key in emotions:
        f.write(f"{key}: {emotions[key]} ({emotions[key]/len(comment_list)*100:.2f}%)\n")

    # Close the file
    f.close()

    # Return the most common emotion
    return highest_emotion
