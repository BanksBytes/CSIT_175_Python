#!/usr/bin/env python3

counter = 0
score_total = 0
test_score = 0
number_scores = 5  # Set the maximum number of test scores

while counter < number_scores:
    test_score = int(input("Enter test score: "))
    if 0 <= test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Invalid score. Please enter a score between 0 and 100.")

average_score = round(score_total / counter) if counter > 0 else 0

print("===============")
#print("Tests taken: " + str(number_scores) + "\nAverage Score: " + str(average_score)) # Testing out f" down below

print(f"Tests taken: {number_scores}\n"
      f"Average Score: {average_score}")
