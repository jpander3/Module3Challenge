# Python Code for PyPoll

import csv
import os

election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

total_votes = 0
winner = []

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_votes = total_votes + 1

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------")



print(f"----------------------")
print(f"Winner: ")
print(f"----------------------")

election_data_output = os.path.join("PyPoll", "Analysis", "election_data.txt")
with open(election_data_output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"----------------------\n")



    txtfile.write(f"----------------------\n")
    txtfile.write(f"Winner: \n")
    txtfile.write(f"----------------------\n")
