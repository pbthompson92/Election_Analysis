#The data we need to retrieve. 
import csv
import os

#Assign a variable for the file to load and the path 
# direct methond - file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file
file_to_save = os.path.join("Analysis", "election_results.txt")

#Open the election results and read the file
#with open(file_to_save, "w") as txt_file:
with open(file_to_load) as election_data:

    #Write some data to the file
    #txt_file.write("Counties in the Election\n---------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    #Read and Analyze Data
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file
    #for row in file_reader:
        #print(row)

#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote