import streamlit as st
import time
from geopy.geocoders import Nominatim
import math
import twilio
import random
from twilio.rest import Client

st.set_page_config(layout="wide")


st.header("SHOPPING APP")


OTP = random.randint(1000, 9999)

# Initialize session state for each button
if "button1" not in st.session_state:
    st.session_state["button1"] = False
if "button2" not in st.session_state:
    st.session_state["button2"] = False
if "button3" not in st.session_state:
    st.session_state["button3"] = False







col1, col2 = st.columns(2)



with col1:
    st.image("https://m.media-amazon.com/images/I/71H0vxwB3PL._SX569_.jpg")
    st.text("PRICE::$1621")
    st.page_link("pages/buynow.py", label="BUY NOW")





    if st.session_state["button1"]:
        name = st.text_input("Enter your Full name")
        text = st.text_input("Enter your Card details")
        mobile=st.text_input("Enter your mobile number")
        cvv = st.text_input("Enter your CVV")
        address=st.text_input("Enter your Address")




        if st.button("DISPLAY DEATAILS and PAY NOW"):
            #st.write(name,text,address

            if(name=="Adarsh" and text=="123456" and cvv=="888"):
                st.session_state["button2"] = not st.session_state["button2"]
                with st.spinner('Wait for it...'):
                    time.sleep(5)
                st.success('OTP SEND SUCCESSFULLY')
                #otp or link sending work
            else:
                st.header("Please Enter Correct Card Details")

            # st.write(OTP)
            account_sid = 'ACa395fb7ffab5fd7d43872a369e4d7301'
            auth_token = '3dcd625909d1749334e3c26032fbcca2'

            client = Client(account_sid, auth_token)
            msg = client.messages.create(body="Share the OPT carefully   " + str(OTP),
                                         from_='+1 209 882 4995',
                                         to="+91"+mobile)
            # st.write(msg.sid)

        if st.session_state["button2"]:
            otp = st.text_input(label="OTP")
            if st.button("Submit"):
                st.session_state["button3"] = not st.session_state["button3"]
                if st.session_state["button3"]:
                    st.write(otp)

                    if otp!=OTP:
                        st.success("Payment Done")
                        st.balloons()
                    else:
                        st.warning("Otp Not Matched")






with col2:
    st.image("https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mba15-spacegray-config-202306?wid=840&hei=508&fmt=jpeg&qlt=90&.v=1684340991372")
    st.text("PRICE::$1297")
    st.button("Buy now")



col3, col4 = st.columns(2)
with col3:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")
    st.text("PRICE::$385")
    st.button("Buy Now")

with col4:
    st.image("https://d2xamzlzrdbdbn.cloudfront.net/products/8df0b70d-0d4b-4d41-9bd1-cc1caf78e7b822291121.jpg")
    st.text("PRICE::$1368")
    st.button("Buy NOw")


col5, col6 = st.columns(2)
with col5:
    st.image("https://m.media-amazon.com/images/I/71BlZZ2w16L._SX569_.jpg")
    st.text("PRICE::$1800")
    st.button("BUy Now")

with col6:
    st.image("https://m.media-amazon.com/images/I/51GGNToj7aL._SX569_.jpg")
    st.text("PRICE::$1141")
    st.button("BuY NOw")


col7, col8 = st.columns(2)
with col7:
    st.image("https://m.media-amazon.com/images/I/81MQOV40FbL._SX569_.jpg")
    st.text("PRICE::$1140")
    st.button("buy Now")

with col8:
    st.image("https://m.media-amazon.com/images/I/415VfHxMlXL._SX300_SY300_QL70_FMwebp_.jpg")
    st.text("PRICE::$1200")
    st.button("bUy NOw")

col9, col10 = st.columns(2)
with col9:
    st.image("https://m.media-amazon.com/images/I/71-4uiO4ZCL._SX569_.jpg")
    st.text("PRICE::$1668")
    st.button("buY Now")

with col10:
    st.image("https://m.media-amazon.com/images/I/71FE4cemJ9L._SX569_.jpg")
    st.text("PRICE::$1081")
    st.button("buy NOw")

col11, col12 = st.columns(2)
with col11:
    st.image("https://d2xamzlzrdbdbn.cloudfront.net/products/8df0b70d-0d4b-4d41-9bd1-cc1caf78e7b822291121.jpg")
    st.text("PRICE::$1160")
    st.button("buy NoW")

with col12:
    st.image("https://m.media-amazon.com/images/I/61+r3+JstZL._SX679_.jpg")
    st.text("PRICE::$540")
    st.button("Buy Nw")
