import time
import streamlit as st
from hotel import Hotel, DownloadableTicket, SpaHotel, HOTELS
from cards import pay, authenticate

"""This code is written by GamerXZEN on behalf of G&SNN Co"""
"""The owner of these hotels is G&SNN FE Estates FAIRCO"""

st.set_page_config(page_title="Book Hotels", initial_sidebar_state="auto",
                   layout="wide", page_icon="18.png")

st.title("Hotel Booking App")
st.write(HOTELS)
hotel_global_id = st.text_input("Enter Hotel ID: ")
name = st.text_input("Enter your name: ")
hotel_type = st.selectbox("Select your hotel type", ("Normal", "Spa"))

if hotel_global_id:
	if name:
		if hotel_type == "Normal":
			hotel = Hotel(hotel_global_id)
			if hotel.available():
				card_number = st.text_input("Enter your card number: ",
				                            placeholder="Example: "
				                                        "4444-4444-4444-4444")
				if len(card_number.strip("-")) < 16:
					st.error("Card number is invalid")
				else:
					expiration = st.text_input("Enter your expiration date: ",
					                           placeholder="Example: 04/24")
					if expiration.find("/"):
						cvc = st.text_input("Enter your CVC/CVV: ",
						                    placeholder="Example: 956")
						if len(cvc) == 3 and int(cvc):
							holder = st.text_input("Enter the cardholder's name: ",
							                       placeholder="Example: John Smith")
							if holder.find(" "):
								name = st.text_input("Enter name")
								password = st.text_input("Enter your password")
								if name:
									if password:
										if authenticate(name, password):
											button = st.button("Submit Information")
											if button:
												st.success("Success")
												print("Success")
												st.write(pay())
										else:
											st.error("Name and password do not "
											         "match with database.")
							else:
								st.error("Cardholder name is invalid")
						else:
							st.error("CVC/CVV is invalid")
					else:
						st.error("Expiration date is invalid.")
				button = st.button("Proceed to download")
				if button:
					hotel.book()
					ticket = DownloadableTicket(hotel_global_id, name)
					ticket.gen_ticket()
					with open("ticket.pdf", "rb") as file:
						out_pdf = file.read()
					progress_text = "Operation in progress. Please wait."
					my_bar = st.progress(0, text=progress_text)
					for percent_complete in range(100):
						time.sleep(0.1)
						my_bar.progress(percent_complete + 1, text=progress_text)
						if percent_complete >= 99:
							st.success("Operation complete")
					st.snow()
					st.download_button("Download DownloadableTicket", data=out_pdf,
					                   file_name="ticket.pdf")
			else:
				st.warning("Hotel cannot be booked because it is full.")
		else:
			spa_hotel = SpaHotel(hotel_global_id)
			if spa_hotel.available():
				card_number = st.text_input("Enter your card number: ",
				                            placeholder="Example: "
				                                        "4444-4444-4444-4444")
				if len(card_number.strip("-")) < 16:
					st.error("Card number is invalid")
				else:
					expiration = st.text_input("Enter your expiration date: ",
					                           placeholder="Example: 04/24")
					if expiration.find("/"):
						cvc = st.text_input("Enter your CVC/CVV: ",
						                    placeholder="Example: 956")
						if len(cvc) == 3 and int(cvc):
							holder = st.text_input("Enter the cardholder's name: ",
							                       placeholder="Example: John Smith")
							if holder.find(" "):
								name = st.text_input("Enter name")
								password = st.text_input("Enter your password")
								if name:
									if password:
										if authenticate(name, password):
											button = st.button("Submit Information")
											if button:
												st.success("Success")
												print("Success")
												st.write(pay())
										else:
											st.error("Name and password do not "
											         "match with database.")
							else:
								st.error("Cardholder name is invalid")
						else:
							st.error("CVC/CVV is invalid")
					else:
						st.error("Expiration date is invalid.")
				button = st.button("Proceed to download")
				if button:
					spa_hotel.gen_ticket(hotel_global_id, name)
					with open("ticket.pdf", "rb") as file:
						out_pdf = file.read()
					progress_text = "Operation in progress. Please wait."
					my_bar = st.progress(0, text=progress_text)
					for percent_complete in range(100):
						time.sleep(0.1)
						my_bar.progress(percent_complete + 1, text=progress_text)
						if percent_complete >= 99:
							st.success("Operation complete")
					st.snow()
					st.download_button("Download DownloadableTicket", data=out_pdf,
					                   file_name="ticket.pdf")
			else:
				st.warning("Hotel cannot be booked because it is full.")
			

if int(time.strftime("%M")) == 00:
	HOTELS["Available"] = "yes"
	HOTELS.to_csv("hotels.csv", index=False)
