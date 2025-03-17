import streamlit as st  
import random  
import string  

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Uppercase & lowercase letters

    if use_digits:
        characters += string.digits  # Add numbers (0-9)
    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&*)

    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
st.set_page_config(page_title="🔐 Password Generator", page_icon="🔑", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>🔐 Simple Password Generator</h1>", unsafe_allow_html=True)

# Password length slider
length = st.slider("📏 Select password length:", min_value=6, max_value=32, value=12)

# Checkboxes for customization
use_digits = st.checkbox("🔢 Include numbers")
use_special = st.checkbox("🔣 Include special characters")

# Generate button
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"**Your Secure Password:** `{password}`")
