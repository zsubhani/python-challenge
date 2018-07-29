# This is main.py for PyPoll by Zeshaun Subhani

import os
import csv


# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# create empty dictionary for counting votes by Candidate
votes_dict = {}

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
      
    # Skip first row to not look at 'Voter ID', 'County' and 'Candidate' 
    next(csvreader, None)
    
    # Loop through the data
    for row in csvreader:
        
        #make Candidate name the key of the votes dictionary and it will be indexed by data in 3rd column
        key = row[2]
        #If candidate name is in the votes dictionary then increment that candidate's vote count by 1. 
		#If candidate name is not already in the votes dictionary then set the candidate's vote count to 1 (ie that's their first vote)
        if key in votes_dict:
            votes_dict[key] += 1
        else:
            votes_dict[key] = 1

# create function called calc_votes that will pass in the votes dictionary and iterate through key and value of that votes dictionary
# output will be total number of votes in election and returned as an integer value
def calc_votes(d):
	# initialize total votes
    tot_v = 0
	# loop through and add all votes that were in votes dictionary
    for key,value in d.items():
        tot_v = tot_v + value
	# return the value of total votes to use in later parts of script
    return tot_v

# call calc_votes function and store total_votes value to use in later parts of script 
total_votes = calc_votes(votes_dict)

# create function called vote_percent_and_count that will pass in the votes dictionary and total number of votes
# output will be printing of string concatenation showing each candidate's name, corresponding vote percentage, and corresponding number of votes 
def vote_percent_and_count(d, tot_v):
	# loop through all key and values in votes dictionary
    for key, value in d.items():
		# vote percent will be (number of votes value in votes dictionary / total number of votes) * 100 as a float
        vote_percent = ((value/tot_v)* 100)
        # vote_percent_string will be a string formatted of float variable vote_percent to 3 decimal places
        vote_percent_string = format(vote_percent, '.3f')
        #print candidate's name followed by vote percentage and then their total number of votes
        print(key + ": " + vote_percent_string + "% (" + str(value) + ")")

# create function called get_winner that will pass in the votes dictionary
# output will be name of candidate with the highest number of votes in the votes dictionary and will be returned as a string
def get_winner(d):
	# initialize winner_name
    winner_name = ""
	# initialize winner_votes
    winner_votes = 0
	# loop through all key and values in votes dictionary
    for key, value in d.items():
		# if value in votes dictionary at the time is greater than or equal to winner_votes,
		# then winner_votes updates to what value is at the time and winner_name becomes the corresponding key 
        if value >= winner_votes:
            winner_votes = value
            winner_name = key
	# return winner_name as a string to use later in script
    return winner_name

# call get_winner function and store election_winner value to use in later parts of script
election_winner = get_winner(votes_dict)


# print Election Results Summary to screen/terminal
print("Election Results")
print("-------------------------")
# print Total Votes and use total_votes variable which was stored earlier in the script
print("Total Votes: " + str(total_votes))
print("-------------------------")
# call vote_percent_and_count founction to output each candidate's name, vote percentage and their total number of votes
vote_percent_and_count(votes_dict, total_votes)
print("-------------------------")
# print Winner and use election_winner variable which was stored earlier in the script
print("Winner: " + election_winner)
print("-------------------------")

# create function called text_vote_percent_and_count that will pass in the votes dictionary and total number of votes
# output will be printing of string concatenation showing each candidate's name, corresponding vote percentage, and corresponding number of votes 
# only difference here is that the print will be output to a text file instead of to the screen/terminal
def text_vote_percent_and_count(d, tot_v):
	# loop through all key and values in votes dictionary
    for key, value in d.items():
		# vote percent will be (number of votes value in votes dictionary / total number of votes) * 100 as a float
        vote_percent = ((value/tot_v)* 100)
        # vote_percent_string will be a string formatted of float variable vote_percent to 3 decimal places
        vote_percent_string = format(vote_percent, '.3f')
        #print candidate's name followed by vote percentage and then their total number of votes
        print(key + ": " + vote_percent_string + "% (" + str(value) + ")", file=text_file)

# export txt file with Election Results
with open("Election_Results.txt", "w") as text_file:
	print("Election Results", file=text_file)
	print("-------------------------", file=text_file)
	print("Total Votes: " + str(total_votes), file=text_file)
	print("-------------------------", file=text_file)
	# call text_vote_percent_and_count founction to output each candidate's name, vote percentage and their total number of votes to text_file
	text_vote_percent_and_count(votes_dict, total_votes)
	print("-------------------------", file=text_file)
	print("Winner: " + election_winner, file=text_file)
	print("-------------------------", file=text_file)

# End of main.py script

