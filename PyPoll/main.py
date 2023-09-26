import csv
import os
# Initialize variables
file_to_output = os.path.join("analysis", "election_data.txt")
file_to_output = "election_data.txt"
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open("PyPoll/Resources/election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)
    
    for row in csvreader:
        voter_id = row[0]
        candidate = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Find the winner
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
   # print(f"{candidate}: {vote_percentage:.3f}% ({votes})") 


# Calculate and print the results
analysis_text = (
     f"Election Results"
f"Election Results"
f"-------------------------"
f"Total Votes: {total_votes}"
f"-------------------------"

f"-------------------------"
f"Winner: {winner}"
f"-------------------------"
)
 #Print the analysis to the terminal
print(analysis_text)
# Export the analysis to a text file
with open("election_results.txt", 'w') as text_file:
   text_file.write(analysis_text)
print(f"Results exported to {analysis_text}")