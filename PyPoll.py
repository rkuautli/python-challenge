import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  # Skip header row

    # Iterate through the rows in the CSV
    for row in csvreader:
        # Count total number of votes
        total_votes += 1
        
        # Extract candidate name from row
        candidate_name = row[2]
        
        # Add candidate to dictionary if not already present
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Increment candidate's vote count
        candidate_votes[candidate_name] += 1

# Calculate percentage of votes for each candidate
percentages = {}
for candidate in candidate_votes:
    vote_count = candidate_votes[candidate]
    percentage = (vote_count / total_votes) * 100
    percentages[candidate] = round(percentage, 3)

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to text file
output_file = os.path.join("analysis", "election_results.txt")
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidate_votes:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

