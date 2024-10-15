Multiple Text Summarization App
Overview:
This app provides an easy-to-use interface for summarizing various text formats, including .txt, .pdf, .csv, and .html files. It leverages the Hugging Face Transformer model to automatically generate concise summaries of the provided text.

Features:
Multiple File Formats: Users can upload files in .txt, .pdf, .csv, or .html formats for summarization.
Automatic Summarization: The app uses a state-of-the-art NLP model from Hugging Face to generate summaries from the uploaded content.
Text Length Handling: Text longer than 2000 characters is truncated to fit the model’s input size, ensuring efficient summarization.
User-Friendly Interface: Built using Streamlit, the app provides a simple and interactive interface for document upload and summarization.
How It Works:
Upload a Document: Users can upload text files, PDFs, CSVs, or HTML files.
Text Extraction: The app extracts the text content from the uploaded file.
Summarization: After uploading, users can click the "Summarize" button to generate a summary of the text.
Result Display: The original text and the generated summary are displayed on the app's interface.
Technologies Used:
Streamlit: For building the web-based user interface.
Transformers (Hugging Face): For the summarization pipeline.
PyPDF2: For reading and extracting text from PDF files.
Pandas: For handling and extracting text from CSV files.
BeautifulSoup: For extracting text from HTML files.
Torch: Backend support for the Hugging Face model.
Installation:
Clone the repository or download the project files.
Install the necessary libraries.

