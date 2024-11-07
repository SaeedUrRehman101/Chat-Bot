import torch
import streamlit as st
from transformers import pipeline

# Define the text-generation pipeline
pipe = pipeline("text-generation", model="openai-community/gpt2")

# Title of the Streamlit app
st.title("AI Text Generation App")

# Custom CSS for styling input and button
st.markdown(
    """
    <style>
    /* Custom input border and focus style */
    .stTextInput>div>div>input {
        border: 2px solid lightgreen; /* Light green border for input */
    }
    
    /* Remove the red outline on focus */
    .stTextInput>div>div>input:focus {
        outline: none;
        border: 2px solid lightgreen; /* Keep the light green border on focus */
    }

    /* Custom button style */
    .stButton>button {
        background-color: green; /* Green button */
        color: white;  /* White text on the button */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }

    /* Change button color on hover */
    .stButton>button:hover {
        background-color: darkgreen; /* Dark green background on hover */
        color: white; /* Ensure the text color remains white on hover */
    }

    /* Ensure button text color stays white even when clicked */
    .stButton>button:active {
        background-color: darkgreen; /* Keep dark green on click */
        color: white !important; /* Force the text to stay white even when clicked */
    }
    </style>
    """, unsafe_allow_html=True
)

# Text input for prompt
prompt = st.text_input("Enter your prompt:", "What is AI?")

# Check if the input is empty and show a warning message
if st.button("Generate Response"):
    if not prompt.strip():  # If the prompt is empty or just whitespace
        st.warning("Please fill the input field.")  # Display warning message
    else:
        # Set max_length and temperature for the response
        result = pipe(prompt, max_length=300, temperature=0.7, do_sample=True)
        generated_text = result[0]["generated_text"]

        # Display the generated text
        st.subheader("Generated Response:")
        st.write(generated_text)
