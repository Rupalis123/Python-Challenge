#main.py for PyPoll challenge

#importing Python modules to work with CSV files
import os
import csv

#setting up path to collect data from the Resources folder
election_data_path = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

#declaring work lists to store the data for candidates, votes and percentage of votes
#declaring varibales to store total votes and winner
electionDataCSVVotes = []
electionDataCSVCandidate = []
electionDataCSVVotesPercent = []
TotalVotes = 0
Winner = ""

#Read in the CSV data file
with open(election_data_path, 'r') as PyPollFile:
    # split the data on commas
    csvreader = csv.reader(PyPollFile, delimiter=',')
   # reading the header row
    csvheader = next(csvreader)

    #loop through the data
    for row in csvreader:
    #calculate total number of votes using +=, it adds another value with the variable's value and assigns the new value to the variable
        TotalVotes += 1
        #print(f"Total Votes: {TotalVotes}")

#calculate a list of candidates who received votes, this will be unique candidates from the list
        if row[2] not in electionDataCSVCandidate:
            electionDataCSVCandidate.append(row[2])
            electionDataCSVVotes.append(1)
        else:
            electionDataCSVVotes[electionDataCSVCandidate.index(row[2])] += 1

#calculate the percentage of votes for each candidate
#pctVotes = round(((votes/total_votes) * 100), 3)
electionDataCSVVotesPercent = [(100/TotalVotes) * candidatevotes for candidatevotes in electionDataCSVVotes]
electionDataCSVVotesPercent = [(100/TotalVotes) * x for x in electionDataCSVVotes]

#find the winner of the election based on popular vote
Winner = electionDataCSVCandidate[electionDataCSVVotes.index(max(electionDataCSVVotes))]
print(f"Winner is: {Winner}")

#print the analysis to the terminal 
print("Election Results")
print("--------------------------")
print("Total Votes:" + str(TotalVotes))
print("--------------------------")


for candidate in electionDataCSVCandidate:
    print(candidate + ": " + str(format(electionDataCSVVotesPercent[electionDataCSVCandidate.index(candidate)], '.3f')) 
        + "% (" + str(electionDataCSVVotes[electionDataCSVCandidate.index(candidate)]) + ")")
    
print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")


# export a text file with the results
output = open(".\Analysis\PyPollAnalysis.txt", "w")
output.write("Election Results\n")
output.write("--------------------------\n")
output.write("Total Votes: " + str(TotalVotes) + "\n")
output.write("--------------------------\n")
for candidate in electionDataCSVCandidate:
    output.write(candidate + ": " + str(format(electionDataCSVVotesPercent[electionDataCSVCandidate.index(candidate)], '.3f')) 
                    + "% (" + str(electionDataCSVVotes[electionDataCSVCandidate.index(candidate)]) + ")\n")
	
output.write("--------------------------\n")
output.write("Winner:" + Winner + "\n")
output.write("--------------------------\n")
output.close()