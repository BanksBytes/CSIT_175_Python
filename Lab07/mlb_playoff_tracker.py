#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 7 Exercise 4, MLB Postseason 2023 results

# Import necessary libraries
import os
import csv

# Filename of the CSV file containing MLB postseason results
filename = "mlb_postseason_2023_results.csv"

# Function to process the results from the CSV file
def process_results(filename):
    # Initialize an empty dictionary to store team data
    teams = {}
    try:
        # Open the CSV file for reading
        with open(filename, "r") as file:
            # Create a CSV reader object
            csvFile = csv.reader(file)
            # Iterate through each row in the CSV file
            for row in csvFile:
                # Extract data from the row
                date, team1, runs1, team2, runs2 = row
                runs1, runs2 = int(runs1), int(runs2)

                # Update data for Team 1
                if team1 not in teams:
                    teams[team1] = {'runs': runs1, 'wins': 0}
                else:
                    teams[team1]['runs'] += runs1
                if runs1 > runs2:
                    teams[team1]['wins'] += 1
                
                # Update data for Team 2
                if team2 not in teams:
                    teams[team2] = {'runs': runs2, 'wins': 0}
                else:
                    teams[team2]['runs'] += runs2
                if runs2 > runs1:
                    teams[team2]['wins'] += 1

        # Return the dictionary containing team data
        return teams
    except FileNotFoundError:
        # Handle file not found error
        print(f"Unable to find the {filename}, please make sure the file is within the same directory")

# Function to find the team with the most runs scored
def team_with_most_runs(teams):
    most_runs = 0
    most_runs_team = ""
    # Iterate through each team and its data
    for team, data in teams.items():
        # Check if current team has more runs than previously recorded most runs
        if data['runs'] > most_runs:
            most_runs = data['runs']
            most_runs_team = team
    # Return the team with the most runs and its corresponding runs scored
    return most_runs_team, most_runs

# Function to find the team with the least runs scored
def team_with_least_runs(teams):
    least_runs = float('inf')
    least_runs_team = ""
    # Iterate through each team and its data
    for team, data in teams.items():
        # Check if current team has fewer runs than previously recorded least runs
        if data['runs'] < least_runs:
            least_runs = data['runs']
            least_runs_team = team
    # Return the team with the least runs and its corresponding runs scored
    return least_runs_team, least_runs

# Function to find the team with the most wins
def team_with_most_wins(teams):
    most_wins = 0
    most_wins_team = ""
    # Iterate through each team and its data
    for team, data in teams.items():
        # Check if current team has more wins than previously recorded most wins
        if data['wins'] > most_wins:
            most_wins = data['wins']
            most_wins_team = team
    # Return the team with the most wins and its corresponding number of wins
    return most_wins_team, most_wins

# Function to find the team with the least wins
def team_with_least_wins(teams):
    least_wins = float('inf')
    least_wins_team = ""
    # Iterate through each team and its data
    for team, data in teams.items():
        # Check if current team has fewer wins than previously recorded least wins
        if data['wins'] < least_wins:
            least_wins = data['wins']
            least_wins_team = team
    # Return the team with the least wins and its corresponding number of wins
    return least_wins_team, least_wins

# Process the results from the CSV file
teams = process_results(filename)

# Find the team with the most runs scored
most_runs_team, most_runs_score = team_with_most_runs(teams)

# Find the team with the least runs scored
least_runs_team, least_runs_score = team_with_least_runs(teams)

# Find the team with the most wins
most_wins_team, most_wins = team_with_most_wins(teams)

# Find the team with the least wins
least_wins_team, least_wins = team_with_least_wins(teams)

# Display results
print("Team with most runs scored:", most_runs_team, "with", most_runs_score, "runs")
print("Team with least runs scored:", least_runs_team, "with", least_runs_score, "runs")
print("Team with most wins:", most_wins_team, "with", most_wins, "wins")
print("Team with least wins:", least_wins_team, "with", least_wins, "wins")
