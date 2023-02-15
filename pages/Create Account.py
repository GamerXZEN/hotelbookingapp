import time
import streamlit as st
from cards import authenticate, write_info

"""This code is written by GamerXZEN on behalf of G&SNN Co"""
"""The owner of these hotels is G&SNN FE Estates FAIRCO"""

st.set_page_config(page_title="Create Account", initial_sidebar_state="auto")
name = st.text_input("Enter name")
password = st.text_input("Enter password")
if not authenticate(name, password):
	with st.spinner("Creating account"):
		time.sleep(5)
		write_info(name, password, True)
else:
	st.error("Account was already created")
