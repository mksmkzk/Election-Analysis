import csv
import os

# The filenames of the files that we are reading and writing from.\
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Total Votes Cast
total_votes = 0

# A list of all the candidates name
candidate_options = []

# A dictionary containing the candidates vote count
candidate_votes = {}

#Winning Candidate and Count Tracker Variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        #if we dont see the candidates name, we will append it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # We will set the vote to 1
            candidate_votes[candidate_name] = 1
        else:
            # If he is on the list, we will add one to the total
            candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (votes / total_votes) * 100
        candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    txt_file.write(winning_candidate_summary)
            
        
