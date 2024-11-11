import torch
import streamlit as st
from transformers import pipeline

# Define the text-generation pipeline with a compatible model
pipe = pipeline("text-generation", model="gpt2")

# Title of the Streamlit app
st.title("AI Text Generation App")

# Custom CSS for styling input and button
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        border: 2px solid lightgreen;
    }
    
    .stTextInput>div>div>input:focus {
        outline: none;
        border: 2px solid lightgreen;
    }

    .stButton>button {
        background-color: green;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: darkgreen;
    }
    </style>
    """, unsafe_allow_html=True
)

# Text input for prompt with placeholder
prompt = st.text_input("Enter your prompt:", placeholder="What is AI?")

# Check if the input is empty and show a warning message
if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please fill the input field.")
    else:
        # Set max_length and temperature for the response
        result = pipe(prompt, max_length=300, temperature=0.7, do_sample=True)
        generated_text = result[0]["generated_text"]

        # Display the generated text
        st.subheader("Generated Response:")
        st.write(generated_text)
