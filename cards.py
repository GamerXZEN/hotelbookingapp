import csv
import random
import pandas as pd

"""This code is written by GamerXZEN on behalf of G&SNN Co"""
"""The owner of these hotels is G&SNN FE Estates FAIRCO"""


def write_info(holder, password, boolean):
	with open("card_security.csv", "a", newline="") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([holder, password, boolean])


def authenticate(holder, password):
	cards = pd.read_csv("card_security.csv", dtype=str)
	if cards.loc[cards["Name"] == holder, "Bool"].squeeze():
		if cards.loc[cards["Password"] == password, "Bool"].squeeze():
			return True
		else:
			return False
	else:
			return False


def pay():
	return f"${random.randint(10, 50)} was subtracted from " \
	       f"your debit/credit card."
