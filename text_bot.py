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
    .stTextInput>div>div>input {
        border: 2px solid lightgreen; /* Light green border for input */
    }
    .stButton>button {
        background-color: green; /* Green button */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: darkgreen; /* Dark green on hover */
    }
    </style>
    """, unsafe_allow_html=True
)

# Text input for prompt
prompt = st.text_input("Enter your prompt:", "What is AI?")

# Generate text when button is clicked
if st.button("Generate Response"):
    # Set max_length and temperature for the response
    result = pipe(prompt, max_length=300, temperature=0.7, do_sample=True)
    generated_text = result[0]["generated_text"]

    # Display the generated text
    st.subheader("Generated Response:")
    st.write(generated_text)
