# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you thje following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the voter turn out of each county.
3. Calculate the percentage of votes from each county out of the total count.
4. Determine the county with highest turnout.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate won.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code 1.63.2

## Results of the Election Audit
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The voter turnout per county:
  - Jefferson had 10.5% of the vote with 38,855 number of votes.
  - Denver had 82.8% of the vote with 306,055 number of votes.
  - Jefferson had 6.7% of the vote with 24,801 number of votes. 
- The county with the largest turnout:
  - Denver had the largest turnout with 82.8% of the vote and 306,055 number of votes.
- The Candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Summary
  With the code that we have written, we are able to take and expand this to any other election with some modifications. If we had a state-wide election that has multiple issues on the ballot, we would need to modify our script to look at the different columns and keep track of each of the issues being voted on. If we had a multi state election, we can expand our script to not only track the number of votes per counties, but also track the number of votes for each state. In short, for whatever election that we have to track, we can modify this script to report and analyze the results.
