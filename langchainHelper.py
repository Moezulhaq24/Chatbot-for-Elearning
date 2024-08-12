from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os



# Configure API key
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the Google Generative AI client
llm = ChatGoogleGenerativeAI(model = "gemini-pro", google_api_key=api_key)


llm_embeddings = GoogleGenerativeAIEmbeddings(model= "models/embedding-001")

vector_db_file_path = "faiss.index"

def Create_Vector_DB():
    # Load data from faqs sheet
    loader = CSVLoader(file_path='faqs.csv', source_column='prompt')
    data = loader.load()

    # Create a FAISS instance for vector database from data
    vector_db = FAISS.from_documents(documents=data, embedding=llm_embeddings)

    # Save a vector database locally
    vector_db.save_local(vector_db_file_path)

def Get_QA_Chain():
    # Load the vector database from the local folder
    vector_db = FAISS.load_local(vector_db_file_path, embeddings=llm_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vector_db.as_retriever(threshold=0.7)

    # Creating a prompt template for the model
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from the "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": prompt})

    return chain

if __name__ == "__main__":
    Create_Vector_DB()
    chain = Get_QA_Chain()
    print(chain({"query": "Do you have a javascript course?"}))
