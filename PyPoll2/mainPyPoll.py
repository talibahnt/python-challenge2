#Modules import the operating system and the excel file (csv/csv file).
import os
import csv


#Create a path for the csv file to upload
PyPollcsvpath = os.path.join("Resources", "election_data.csv")

#Create lists to store data and set counter values to 0. Total Vote Counter, Candidate Options is a dictionary and Vote Counters.
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning candidate (won the election) and number of Winning Votes Counter.
winning_candidate = ""
winning_votes = 0

#Check path
if not os.path.exists(PyPollcsvpath):
    print(f"Error: The file {PyPollcsvpath} does not exist.")
    exit()

#Open csv file (election_data.csv) using the defined path PyPollcsvpath.
with open(PyPollcsvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Loop through each row in the dataset. Find the total number of months in the dataset. Monitor totals.
    for row in csvreader:
        
        #Add to the total vote count.
        total_votes+= 1
        
        #Pull out the candidate name for each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate, does not match any existing candidate, add to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's number of votes.
        candidate_votes[candidate_name] += 1

#Create output directory if it doesn't exist
output_directory = 'analysis'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
        
#Create a path for the text file to output. Export and display result as a text (.txt) file in Microsoft Word.
PyPoll_output_csvpath = os.path.join(output_directory, 'PyPoll_2_Election_Analysis.txt')
with open(PyPoll_output_csvpath, 'w', newline='') as textfile:

#Print the election results and export the results in the textfile "PyPoll_2_Election_Analysis".
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"

)
print(election_results)
textfile.write(election_results)

#Loop through all of the votes to determine the winning candidate.
for candidate in candidate_votes:

    #Determine the number of votes for each candidate and their voting percentages
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100

    #Determine winning number of votes and candidate
    if votes > winning_votes:
       winning_votes = votes
       winning_candidate = candidate

    #Print each candidate's number of votes and voter percentage
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(voter_output)

    #Save each candidates number of votes and percentages to text file
    textfile.write(voter_output)

#Print the winning candidate
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"------------------------\n"
)
print(winning_candidate_summary)

#Save the winning candidate's name to the text file
textfile.write(winning_candidate_summary)

#Keep getting a ValueError: I/O operation on closed file in line 63: Checked the indentations on the election_results and f-strings.