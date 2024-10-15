# app.py
import streamlit as st
from transformers import pipeline

# Load the summarization pipeline with the specified model
pipe = pipeline("summarization", model="Yihui/t5-small-text-summary-generation")

# Set the title of the app
st.title("Summary Generator")
st.markdown("<p style='color:blue; font-size:20px;'>Developed by Zubair</p>", unsafe_allow_html=True)
st.markdown("<p style='color:red; font-size:15px;'>Based on Hugging Face Model</p>", unsafe_allow_html=True)

# Create a text area for user input
input_text = st.text_area("Enter the text you want to get summarize:", height=200)

# Create a button to trigger the summarization
if st.button("Summarize"):
    if input_text:
        # Generate the summary
        summary = pipe(input_text, max_length=150, min_length=30, do_sample=False)
        
        # Display the summarized text
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
