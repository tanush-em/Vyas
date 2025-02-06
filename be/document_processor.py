from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    chunks = text_splitter.split_text(text)
    return chunks