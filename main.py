import os
import sys
import pymupdf

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

from dspy_module.doc_dspy import dspy_doc
from dspy_module.field_dspy import field_doc


def extract_text_from_pdf(file):
    """
    Extract text from a PDF file.
    """
    doc_text=[]
    try:
        with pymupdf.open(file) as doc:
            for page in doc:
                doc_text.append(page.get_textpage())
        return doc_text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


Doc_Identifier= dspy_doc()
Field_Identifier= field_doc()


ds="dataset/The_Metamorphosis_Franz_Kafka.pdf"
data= extract_text_from_pdf(ds)



