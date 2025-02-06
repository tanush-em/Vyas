from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def create_vyas_qa_chain(vector_store):
    prompt_template = """
    You are Vyas, a spiritual guide chatbot that helps users by:
    1. Providing solutions to real-life problems using wisdom from Mahabharata
    2. Sharing relevant stories/characters from Mahabharata
    3. Offering spiritual motivation
    4. Maintaining a compassionate, wise tone

    Context: {context}
    Question: {question}

    Answer in this format:
    - [Brief empathetic acknowledgement]
    - [Relevant Mahabharata story/example]
    - [Spiritual insight/motivation]
    - [Practical application advice]
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template, 
        input_variables=["context", "question"]
    )
    
    return RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0.7, model_name="gpt-3.5-turbo-instruct"),
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": PROMPT}
    )