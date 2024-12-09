# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate = ''

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}



# Winning Candidate and Winning Count Tracker
winner = ''
winning_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        candidate = row[2]

        # Print a loading indicator (for large datasets)
        print(",", end="")

        # Calculate votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else: 
            candidate_votes[candidate] = 1
        
        # Calculate total votes
        total_votes += 1


    # Print the total vote count (to terminal)
    print(f"-------------------------------------------")
    print(f"Election Results")
    print(f"-------------------------------------------")
    print(f"Total Votes: {total_votes:,}")
    print(f"-------------------------------------------")

    #find the percentage of votes each candidate won
    for candidate, votes in candidate_votes.items():
        candidate_percent = round((votes / total_votes) * 100, 2)
    
        print(f'{candidate}: {candidate_percent:.2f}% ({votes:,})') 
    
    print(f"-------------------------------------------")

    # Find the winner of the election
    for candidate, votes in candidate_votes.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
        
    print(f"Winner: {winner}")
    print(f"-------------------------------------------")

    #Open a text file to save the output
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Election Results\n")
        txt_file.write("--------------------------------------------\n")
        txt_file.write(f"Total Votes: {total_votes:,}\n")
        txt_file.write("--------------------------------------------\n")

        for candidate, votes in candidate_votes.items():
            vote_percentage = round((votes / total_votes) * 100, 2)
            txt_file.write(f"{candidate}: {candidate_percent:.2f}% ({votes:,})\n") 
        
        txt_file.write("--------------------------------------------\n") 

        txt_file.write(f"Winner: {winner}\n")
    
        txt_file.write("--------------------------------------------\n")