# The data we need to retrieve. 
import csv
import os

# Assign a variable for the file to load and the path 
# direct methond - file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file
file_to_save = os.path.join("Analysis", "election_results.txt")

# Initalize the total vote counter 
total_votes = 0 

# Declare candidate list
candidate_options = []

# Create Candidate Votes Dictionary to track votes by candidate 
candidate_votes = {}

# Winning Candidate and Variables
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file
# with open(file_to_save, "W") as txt_file:
with open(file_to_load) as election_data:

    # Write some data to the file
    # txt_file.write("Counties in the Election\n---------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

    # Read and Analyze Data
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes +=1

        # Print candidate name 
        candidate_name = row[2]

        # Add the candidate name to candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the cadidate list
            candidate_options.append(candidate_name)

            # Begin tracking that cadidate's vote count
            candidate_votes[candidate_name] = 0 

        # Add vote every time cadidate name appears
        candidate_votes[candidate_name] += 1

    # Calculate % of votes per candidate
    for candidate_name in candidate_votes: 

        # Retrieve total votes per candidate 
        votes = candidate_votes[candidate_name]

        # calculate vote percentage
        vote_percentage = float(votes)/float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        # print candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if the count of votes is the largest and therefore the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to the terminal 
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"---------------------------\n")

    print(winning_candidate_summary)
        
    
# Print the total votes
# print(total_votes)
# print(candidate_votes)

#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote