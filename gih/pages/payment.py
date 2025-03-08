import streamlit as st
import random
from twilio.rest import Client


st.title("OTP")

OTP = random.randint(1000, 9999)
st.write(OTP)


if st.button("Sign In"):
    mobile="9354235665"
    account_sid = 'AC825bba1c3f92260e14824b8655ffdd23'
    auth_token = 'b0eafb31875a7ec3f0c69674a446f7ea'
    client = Client(account_sid, auth_token)
    msg = client.messages.create(body="Share the OPT carefully   " + str(OTP),
                                 from_='+1 209 882 4995',
                                 to="+91" + mobile)

    st.success("OTP SEND SUCCESFULLY")

otp = st.text_input("otp", max_chars=4, type="password")
st.write(otp)