# imported modules to run analysis
import os as os
import pandas as pd
# setting the path to retrieve the csv file
csvpath_2 = os.path.join("Resources", "election_data.csv")
# creating a data frame to read the raw csv 
df = pd.read_csv("resources/election_data.csv")
# get the total number of values (rows) in the data frame 
total = len(df)
# creating a data frame to house value counts preformed on the original data frame
# its is sorted from highest to smallest values
candidate_count_df = (df["Candidate"].value_counts(ascending = False))
print("Election Results")
print("-------------------------")
print("Total Votes: {} ".format(total))
print("-------------------------")
# sorted the items in the data frame to be sorted alphabetically 
for candidate in sorted(candidate_count_df.items()):
    # {} shows what value to be printed and in what order 
    print("{}: {}% ({})".format(candidate[0], round(candidate[1]/total * 100, 2),candidate[1]))
print("-------------------------")
# next returns only the first item in a list
print("Winner: {}".format((next(candidate_count_df.items()) [0])))
print("-------------------------")
    file.write("-------------------------\n")
    for candidate in candidate_votes:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
