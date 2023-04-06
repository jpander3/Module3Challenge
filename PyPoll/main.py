# Python Code for PyPoll

#Import the csv and os Modules
import csv
import os

#Set a path that leads to the election_data.csv
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Set variables to gather pertinent information
total_votes = 0
cand_names = {}
winner = []

#Open the path that leads to the budget_data.csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Store the header of budget_data.csv
    csv_header = next(csv_reader)

    #Start a loop to look for pertinent information within budget_data.csv
    for row in csv_reader:

        #Count the number of total votes for the election
        total_votes = total_votes + 1

        #Collect the vote for each individual
        name = row[2]

        #Count the number of votes per candidate
        if name in cand_names:
            cand_names[name] += 1
        else:
            cand_names[name] = 1

#Calculate the vote percentage for each candidate
cand_names["Charles Casper Stockham Percent"] = round((cand_names["Charles Casper Stockham"]/total_votes) * 100, 3)
cand_names["Diana DeGette Percent"] = round((cand_names["Diana DeGette"]/total_votes) * 100, 3)
cand_names["Raymon Anthony Doane Percent"] = round((cand_names["Raymon Anthony Doane"]/total_votes) * 100, 3)

#Find the winner corresponding to the candidate with the greatest number of votes
winner = max(cand_names, key=cand_names.get)
        
#Print the analysis to the terminal
print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------")
print(f"Charles Casper Stockham: {cand_names['Charles Casper Stockham Percent']}% ({cand_names['Charles Casper Stockham']})")
print(f"Diana DeGette: {cand_names['Diana DeGette Percent']}% ({cand_names['Diana DeGette']})")
print(f"Raymon Anthony Doane: {cand_names['Raymon Anthony Doane Percent']}% ({cand_names['Raymon Anthony Doane']})")
print(f"----------------------")
print(f"Winner: {winner}")
print(f"----------------------")

#Export a text file with the analysis
election_data_output = os.path.join("PyPoll", "Analysis", "election_data.txt")
with open(election_data_output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Charles Casper Stockham: {cand_names['Charles Casper Stockham Percent']}% ({cand_names['Charles Casper Stockham']})\n")
    txtfile.write(f"Diana DeGette: {cand_names['Diana DeGette Percent']}% ({cand_names['Diana DeGette']})\n")
    txtfile.write(f"Raymon Anthony Doane: {cand_names['Raymon Anthony Doane Percent']}% ({cand_names['Raymon Anthony Doane']})\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"----------------------\n")
