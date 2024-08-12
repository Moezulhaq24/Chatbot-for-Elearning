# E-learning Chatbot

**Udemy Q&A:** Question and Answer System Based on Google Palm LLM and Langchain for E-learning Company

This project is an end-to-end LLM-based question and answer system for an e-learning company, Udemy. It utilizes Google Palm LLM and Langchain to provide a Streamlit-based user interface for students, allowing them to ask questions and receive answers quickly.

## Project Highlights

- **Live Demo:** [E-learning Chatbot Live Demo](https://chatbot-for-elearning.streamlit.app/)
- **Real CSV File Integration:** Uses a real CSV file of FAQs from Udemy.
- **LLM-Based Q&A:** Reduces the workload of human staff by providing instant answers to student queries.
- **Learning Outcomes:**
  - Langchain + Google Palm: LLM-based Q&A
  - Streamlit: User Interface (UI)
  - Huggingface Instructor Embeddings: Text embeddings
  - FAISS: Vector database

## Installation

1. **Clone this repository** to your local machine:

   ```bash
   git clone (https://github.com/Moezulhaq24/Chatbot-for-Elearning.git)

2. **Navigate to the project directory:**

cd elearning-chatbot

3. **Install the required dependencies using pip:**

pip install -r requirements.txt

4. **Acquire an API key** through https://ai.google.dev/aistudio and add it to a .env file:
API_KEY="your_api_key_here"

**Usage**
Run the Streamlit app by executing:
streamlit run main.py
The web app will open in your browser.

Create a knowledge base of FAQs by clicking on the "Create Knowledge Base" button. This process may take some time.

Once the knowledge base is created, you will see a directory called faiss_index in your current folder.

Ask questions by typing them into the question box and pressing Enter.

# Sample Questions
Do you guys provide internship and also do you offer EMI payments?
Do you have a JavaScript course?
Should I learn Power BI or Tableau?
I've a MAC computer. Can I use Power BI on it?
I don't see Power Pivot. How can I enable it?

# Project Structure
main.py: The main Streamlit application script.
langchainHelper.py: Contains all the Langchain code.
requirements.txt: A list of required Python packages for the project.
.env: Configuration file for storing your Google API key. 
