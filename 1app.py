import streamlit as st
from transformers import pipeline
import pandas as pd
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Add the title of the app
st.title("Multiple Text Summarization App")

# Add text instruction
st.write("Upload your document below for summarization:")

# File uploader that accepts txt, pdf, csv, and html files
uploaded_file = st.file_uploader("Choose a text, pdf, csv, or html file", type=["txt", "pdf", "csv", "html"])

# Check if a file has been uploaded
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]  # Get the file extension

    # Handle txt files
    if file_type == "txt":
        text = uploaded_file.read().decode("utf-8")

    # Handle pdf files
    elif file_type == "pdf":
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    # Handle csv files (extract text from the first column)
    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        text = df.iloc[:, 0].to_string(index=False)  # Convert the first column to string

    # Handle html files
    elif file_type == "html":
        html_content = uploaded_file.read()
        soup = BeautifulSoup(html_content, "html.parser")
        text = soup.get_text()  # Extract text from HTML

    # Display the original text
    st.subheader("Original Text")
    st.write(text)

    # Check if the text is too long
    if len(text) > 2000:  # Adjust length based on model token limits
        st.warning("The uploaded text is too long. It will be truncated for summarization.")
        text = text[:2000]  # Truncate text to fit model input size

    # Add a button for summarization
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            try:
                # Generate summary
                summary = summarizer(text, max_length=200, min_length=100, do_sample=False)
                
                # Display the summary
                st.subheader("Summary")
                st.write(summary[0]['summary_text'])
            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")
