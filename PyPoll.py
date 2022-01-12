import csv
import os

# The filenames of the files that we are reading and writing from.\
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")


with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)


with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")    
    txt_file.write("Arapahoe \nDenver \nJefferson")

# 1. The total number of votes cast

# 2. A complete list of candidates

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based of popular vote
