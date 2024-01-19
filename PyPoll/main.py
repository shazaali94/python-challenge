import csv
import os

# Initialize variables
file_to_output = os.path.join("analysis", "election_data.txt")
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

# Calculate and format the results
analysis_text = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Calculate and add the results for each candidate
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    analysis_text += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

# Add the winner to the analysis
analysis_text += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the analysis to the terminal
print(analysis_text)

# Export the analysis to a text file
with open(file_to_output, 'w') as text_file:
    text_file.write(analysis_text)

print(f"Results exported to {file_to_output}")
