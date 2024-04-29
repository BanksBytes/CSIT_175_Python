#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 7 Excercise 1, LyricsAnalyzer - read text file and count occurrence of strings

import os # needed to list files in local directory
import csv # user for formatted output
import Methods

# let user select input file. Return file name.
def select_file():
    file_number = 0
    print()
    print("  ---- found files: ----")
    # display list of local text (.txt) files for user to select
    text_files = [file for file in os.listdir('.') if file.endswith('.txt')]
    for filename in text_files:
        file_number += 1
        print(f"{file_number}: {filename}")

    selection = int(input("select a file by number to process: "))
    return text_files[selection-1]

# read file and return list of strings (words)
def read_lyrics_file(filename):
    with open(filename, "r") as file:
        return file.read().split()
    
# find a number of occurences of each string in the input list
def get_counts(word_list):
    max_count = 0
    unique_words = []
    counts = []

    for word in word_list:
        index = Methods.find_string(unique_words, word)
        if index < 0:
            unique_words.append(word)
            counts.append(1)
        else:
            counts[index] += 1

    total_word_count = len(word_list)
    distinct_word_count = len(unique_words)
    max_count = Methods.max_value(counts)
    most_common_word = "'" + unique_words[counts.index(max_count)] + ""

    # just for fun lets return a tuple
    return (total_word_count, distinct_word_count, most_common_word, max_count)

# display findings to console
def display_results(ttl, unique, most_used, occurrences):
    print()
    print(f"{ttl} words found in the file")
    print(f"{unique} unique words found.")
    print(f"Most common word used : {most_used}, {occurrences} times.")
    print()

# add results to csv file
def add_results(output, results):
    with open(output, "a") as report:
        csv_report = csv.writer(report)
        csv_report.writerow(results)
        report.close()

if __name__ == "__main__":
    output_file = "word_counts.csv"
    input_file_name = select_file()

    # returns a tuple
    (ttl, distinct, most, count) = get_counts(
        read_lyrics_file(input_file_name))
    
    # build results as a list
    results = []
    results.append(input_file_name)
    results.append(ttl)
    results.append(distinct)
    results.append(most)
    results.append(count)

    display_results(ttl, distinct, most, count)

    add_results(output_file, results)
