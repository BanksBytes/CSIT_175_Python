#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 7 Excercise 2, Vote counter


def count_votes(vote_list):
    
    vote_counts = {}
    # open the votes.txt file and read the votes
    with open("votes.txt", "r") as file:
        # Read the lines in the file
        for line in file:
            # set the person value to the person on the line
            person = line
            # Increment the vote count for the person
            vote_counts[person] = vote_counts.get(person, 0) + 1

        return vote_counts


def announce_winner(vote_counts):
    # Find the person(s) with the most votes
    max_votes = max(vote_counts.values())
    winners = [person for person, votes in vote_counts.items() if votes == max_votes]

    # Print the total vote count for each person
    for person, votes in vote_counts.items():
        print(f"{person}: {votes} votes", )

    # If there's a clear winner, print the winner
    if len(winners) == 1:
        print(f"\nThe winner is: {winners[0]} with {max_votes} votes!")
    else:
        print("\nIt's a tie! Multiple people received the same number of votes.")


if __name__ == "__main__":
    voting_file = "voting_results.txt"
    vote_counts = count_votes(voting_file)
    announce_winner(vote_counts)

