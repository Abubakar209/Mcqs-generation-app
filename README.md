# MCQ Generator using Gemini 1.5 Flash Model API and Streamlit
# Overview
This project is a simple yet powerful application that generates multiple-choice questions (MCQs) from a PDF book using the Gemini 1.5 Flash model API and Streamlit. The application demonstrates the potential of generative AI in the educational space, allowing users to upload any PDF document and automatically create MCQs, which can be used for assessments, study guides, or interactive learning.

# Features
PDF Upload: Users can upload any PDF document directly through the web interface.
Automatic MCQ Generation: The app extracts content from the PDF and generates multiple-choice questions using the Gemini 1.5 Flash model API.
Streamlit Interface: A user-friendly interface built with Streamlit that makes it easy to interact with the app.
Real-time Generation: Get MCQs generated instantly after uploading the PDF.
# Requirements
To run this project, you'll need the following:

Python 3.7 or later
Gemini 1.5 Flash model API key
Streamlit
PyPDF2 (or any other library for PDF processing)
Requests library (for API calls)
Python Libraries
You can install the necessary libraries using pip:

bash
Copy code
pip install streamlit pypdf2 requests
Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/mcq-generator.git
cd mcq-generator
Install the Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Your API Key:
Obtain your Gemini 1.5 Flash model API key and set it as an environment variable or directly in the code.

Run the Application:

bash
Copy code
streamlit run app.py
Upload a PDF File:
Once the app is running, you can upload a PDF file, and the MCQs will be generated in real time.

# Usage
Navigate to the Streamlit app on your local machine (usually http://localhost:8501).
Upload your desired PDF file.
The app will process the content and generate MCQs.
Review the generated MCQs and use them as needed.
Obtaining Gemini 1.5 Flash Model API Key
To use the Gemini 1.5 Flash model API, you need an API key. You can obtain this key by signing up on the Gemini platform and accessing their API services. Once you have the key, add it to your environment variables or directly in the code (not recommended for security reasons).

# Future Enhancements
Some potential enhancements for this project include:

Customizable Question Formats: Allow users to customize the type of questions generated.
Support for More Document Types: Expand support to other file formats like Word, text, etc.
Improved Question Quality: Further fine-tuning of the AI model to improve the relevance and quality of generated questions.
Export Options: Add functionality to export the generated MCQs to formats like CSV, PDF, or Quiz platforms.
Contributing
Contributions are welcome! If you have suggestions or would like to contribute to this project, feel free to open a pull request or submit issues.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments
Gemini AI for their powerful Flash model API.
The open-source community for providing invaluable tools and resources.
