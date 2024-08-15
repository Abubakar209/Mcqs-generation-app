import json
import requests
import PyPDF2
import streamlit as st

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# Function to generate MCQs using Gemini 1.5 Flash model
def generate_response(prompt, api_key):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to create a prompt to generate MCQs with proper format
def create_mcq_prompt_with_format(text):
    prompt = (
        "Generate multiple-choice questions (MCQs) with four options from the following text. "
        "Format each question with four options labeled a, b, c, and d, and ensure the formatting resembles online test questions. "
        "Provide each MCQ in the following format:\n\n"
        "Q1: [Question Text] \n"
        "a. [Option A] \n"
        "b. [Option B] \n"
        "c. [Option C] \n"
        "d. [Option D] \n\n"
        "Q2: [Question Text] \n"
        "a. [Option A] \n"
        "b. [Option B] \n"
        "c. [Option C] \n"
        "d. [Option D] \n\n"
        f"{text}\n"
    )
    return prompt

# Streamlit app
def main():
    st.title("MCQ Generator from PDF")

    # Upload PDF
    pdf_file = st.file_uploader("Upload a PDF", type="pdf")

    if pdf_file:
        st.write("Processing the PDF...")

        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(pdf_file)
        
        if pdf_text:
            st.write("Generating MCQs...")
            
            # Create prompt for generating MCQs with proper format
            prompt = create_mcq_prompt_with_format(pdf_text)
            
            # Replace with your actual API key
            api_key = 'your api key'
            
            # Generate MCQs using Gemini 1.5 Flash model
            response = generate_response(prompt, api_key)
            
            if response:
                # Print the full response for debugging
                st.write("Full API Response:")
                st.json(response)
                
                # Extract and display MCQs
                try:
                    mcqs_text = response.get('contents', [])[0].get('parts', [])[0].get('text', 'No text found')
                    st.write("Generated MCQs with Proper Format:")
                    st.text(mcqs_text)
                except (IndexError, KeyError) as e:
                    st.error(f"Error extracting MCQs from response: {e}")
            else:
                st.error("Failed to generate MCQs.")
        else:
            st.error("Failed to extract text from PDF.")

if __name__ == "__main__":
    main()
