from fpdf import FPDF
import pandas as pd
import time
from abc import ABC, abstractmethod

"""This code is written by GamerXZEN on behalf of G&SNN Co"""
"""The owner of these hotels is G&SNN FE Estates FAIRCO"""

HOTELS = pd.read_csv("hotels.csv", dtype={"ID": str})


class Hotel:
	def __init__(self, hotel_id):
		self.hotel_id = hotel_id

	def book(self):
		HOTELS.loc[HOTELS["ID"] == self.hotel_id, "Available"] = "no"
		HOTELS.to_csv("hotels.csv", index=False)

	def available(self):
		availability_loc = HOTELS.loc[
			HOTELS["ID"] == self.hotel_id, "Available"].squeeze()
		if availability_loc == "yes":
			return True
		else:
			return False

	def __eq__(self, other):
		if self.hotel_id == other.hotel_id:
			return True
		else:
			return False


class AbstractTicket(ABC):

	@abstractmethod
	def __init__(self, hotel_loc, user):
		pass

	@abstractmethod
	def gen_ticket(self):
		pass


class DownloadableTicket(AbstractTicket):
	def __init__(self, hotel_loc, user: str):
		self.hotel = hotel_loc
		self.name = user.strip().title()

	def gen_ticket(self):
		pdf = FPDF()
		pdf.add_page(orientation="")
		pdf.set_font(family="helvetica", size=12, style="B")
		pdf.cell(w=0, h=12, txt=f"Name of customer: {self.name}", ln=1,
		         border=1)
		pdf.cell(w=0, h=12, txt=f"Hotel ID: {self.hotel}", border=1, ln=1)
		pdf.cell(w=0, h=12, txt=f"Hotel Name: "
		                        f"{HOTELS.loc[HOTELS['ID'] == self.hotel, 'Name'].squeeze()}",
		         border=1, ln=1)
		pdf.cell(w=0, h=12, txt="Hotel Type: Normal", border=1, ln=1)
		pdf.set_font(family="helvetica", size=8, style="B")
		pdf.cell(w=0, h=8, txt=f"Generated at "
		                       f"{time.strftime('%Y/%m/%d-%I:%M:%S')}", ln=1)
		pdf.cell(w=0, h=8, txt="Made by GamerXZEN & G&SNN Co.")
		pdf.output("ticket.pdf")


class SpaHotel(Hotel):
	@staticmethod
	def gen_ticket(hotel_id, name):
		pdf = FPDF()
		pdf.add_page(orientation="")
		pdf.set_font(family="helvetica", size=12, style="B")
		pdf.cell(w=0, h=12, txt=f"Name of customer: {name}", ln=1,
		         border=1)
		pdf.cell(w=0, h=12, txt=f"Hotel ID: {hotel_id}", border=1, ln=1)
		pdf.cell(w=0, h=12, txt=f"Hotel Name: "
		                        f"{HOTELS.loc[HOTELS['ID'] == hotel_id, 'Name'].squeeze()}",
		         border=1, ln=1)
		pdf.cell(w=0, h=12, txt="Hotel Type: Spa", border=1, ln=1)
		pdf.set_font(family="helvetica", size=8, style="B")
		pdf.cell(w=0, h=8, txt=f"Generated at "
		                       f"{time.strftime('%Y/%m/%d-%I:%M:%S')}",
		         ln=1)
		pdf.cell(w=0, h=8, txt="Made by GamerXZEN & G&SNN Co.")
		pdf.output("ticket.pdf")
