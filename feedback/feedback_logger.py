import csv
import sys

transaction = input("Enter transaction: ")
predicted = input("Predicted category: ")
corrected = input("Correct category: ")

with open('feedback/feedback_log.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([transaction, predicted, corrected])

print("Feedback logged.")
