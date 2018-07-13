# Import os & pandas modules
import os as os
import pandas as pd

# Create absolute file path to data file
file_path = "C:\\Users\\andre\\Documents\\WashU\\WASHSTL201806DATA4-Class-Repository-DATA\\Week 3 - Python\\Homework\\PyPoll\\Resources\\election_data.csv"

# Read in file as pandas dataframe
df = pd.read_csv(file_path)

# Look at data structure
df.head()

# Tally up total votes cast
votes_cast = len(df["Voter ID"].unique())
print(votes_cast)

# Count the number of votes for each candidate
candidates = df["Candidate"].unique()
print(candidates)

# Group by candidate and then count the number of votes for each candidate
votes = df.groupby("Candidate")["Voter ID"].nunique()

# Calculate the share ot total votes for each candidate
vote_share = 100*votes/votes_cast

# Create a new variable that cleans up the vote share variable into a nice string
vote_share_table = vote_share.round(1).astype(str) + '%'
print(vote_share_table)

# Create a pandas dataframe of candidates with their vote share and total votes
vote_summary_table = pd.DataFrame({
                                    "Vote Share": vote_share_table,
                                    "Votes": votes})
print(vote_summary_table)

# Return the candidate with the most votes and save name as winner
winner = votes.idxmax()

# Print a summary table of the election results
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes_cast}")
print("--------------------------------")
print(vote_summary_table.to_string())
print("--------------------------------")
print(f"Winner: {winner}")

# Save summary table as a text file
# Create a text file with the summary and save it
with open("pyPoll_Summary.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("--------------------------------", file=text_file)
    print(f"Total Votes: {votes_cast}", file=text_file)
    print("--------------------------------", file=text_file)
    print(vote_summary_table.to_string(), file=text_file)
    print("--------------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
