from langchain_community.document_loaders import PyPDFLoader
from docx import Document

def load_cv(file_path):
    """
    Loads text content from a PDF CV file using PyPDFLoader.
    :param file_path: Path to the PDF file
    :return: Combined text content of all pages
    """
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return "\n".join(page.page_content for page in pages)

def write_to_docx(text, output_dir='meshion', filename='cover_letter.docx'):
    """
    Writes plain text to a Word document (.docx), one paragraph per line.
    :param text: Text to write
    :param output_dir: Directory to save the docx
    :param filename: File name for the docx
    :return: Full path to saved file
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = Document()
    for para in text.strip().split('\n'):
        if para.strip():
            doc.add_paragraph(para.strip())

    file_path = os.path.join(output_dir, filename)
    doc.save(file_path)
    return file_path
