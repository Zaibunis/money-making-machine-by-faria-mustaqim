import streamlit as st
import random
import time
import requests

# Get API URLs from secrets or use localhost as fallback
HUSTLE_URL = st.secrets["HUSTLE_URL"] if "HUSTLE_URL" in st.secrets else "http://127.0.0.1:8000/side_hustles"
QUOTES_URL = st.secrets["QUOTES_URL"] if "QUOTES_URL" in st.secrets else "http://127.0.0.1:8000/money_quotes"

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.warning(f"You made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get(HUSTLE_URL)
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return "Freelancing"
    except Exception as e:
        print(f"Error: {e}")
        return "Something went wrong!"

# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):  # When user clicks button
    idea = fetch_side_hustle()  # Get a hustle idea
    st.success(idea)  # Show the idea

# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        response = requests.get(QUOTES_URL)
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return "Money is the root of all evil!"
    except Exception as e:
        print(f"Error: {e}")
        return "Something went wrong!"

# Create a section for motivation quotes
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):  # When user clicks button
    quote = fetch_money_quote()  # Get a quote
    st.info(quote)  # Show the quote