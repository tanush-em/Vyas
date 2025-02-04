import fitz  # PyMuPDF

def pdf_to_text(pdf_path, text_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        
        with open(text_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        
        print(f"Text extracted from pdf and saved to {text_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    pdf_path = "/home/tanush/Documents/repos/Vyas/data/unabridged_mahabharata_eng.pdf"  
    text_path = "/home/tanush/Documents/repos/Vyas/data/raw_dt.txt" 
    pdf_to_text(pdf_path, text_path)
