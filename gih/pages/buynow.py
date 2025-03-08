import streamlit as st
from twilio.rest import Client
import random

# Set the page configuration
st.set_page_config(
    page_title="Card Details Form",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="auto"
)

# Generate an OTP
OTP = random.randint(1000, 9999)

# Streamlit layout
st.title("💳 Card Details Form")

# Form inputs
name = st.text_input("Name on Card")
card_number = st.text_input("Card Number", max_chars=16)
expiry_date = st.text_input("Expiry Date (MM/YY)")
cvv = st.text_input("CVV", max_chars=3, type="password")

# Submit button
if st.button("Submit Payment"):
    if not name or not card_number or not expiry_date or not cvv:
        st.error("Please fill in all fields.")
    else:
        try:
            # Send OTP via Twilio
            mobile = "9354235665"  # Replace with user input or hardcoded value
            account_sid = 'AC825bba1c3f92260e14824b8655ffdd23'
            auth_token = 'b0eafb31875a7ec3f0c69674a446f7ea'
            client = Client(account_sid, auth_token)
            msg = client.messages.create(
                body=f"Your OTP is: {OTP}",
                from_='+1 209 882 4995',
                to="+91" + mobile
            )
            st.success(f"OTP sent successfully to +91{mobile}")
        except Exception as e:
            st.error(f"Error sending OTP: {e}")
