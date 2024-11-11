import os
import gradio as gr
from groq import Groq

# Set up Groq API client (ensure GROQ_API_KEY is set in your environment)
GROQ_API_KEY = "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"  # Make sure this is set in your environment
# if not api_key:
#     raise ValueError("GROQ_API_KEY is not set in your environment")
client = Groq(api_key=GROQ_API_KEY)

# Function to get LLM response from Groq
def get_llm_response(prompt):
    try:
        print(f"Sending to Groq LLM: {prompt}")
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",  # Use Groq's supported model
        )
        llm_response = chat_completion.choices[0].message.content
        return llm_response
    except Exception as e:
        print(f"Error in getting LLM response: {e}")
        return f"Error in LLM response: {str(e)}"

# Function to generate text using Groq
def generate_text(prompt):
    if not prompt.strip():
        return "Please enter a valid prompt."
    
    # Get LLM response from Groq
    generated_text = get_llm_response(prompt)
    return generated_text

# Gradio interface for text generation using Groq
iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(label="Enter your prompt:", placeholder="What is AI?", lines=2),
    outputs=gr.Textbox(label="Generated Response:", interactive=False),
    title="AI Text Generation App with Groq",
    description="This app uses Groq's LLM to generate text based on your input prompt.",
    theme="default",  # Use the default Gradio theme
    allow_flagging="never"  # Disables flagging option
)

# Launch the Gradio app
iface.launch()
