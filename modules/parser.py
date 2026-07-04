import re
import PyPDF2


def extract_resume_text(pdf_path):
    """
    Extract text from a PDF resume.
    """

    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


def clean_text(text):
    """
    Clean resume text.
    """

    text = text.lower()

    text = re.sub(r'http\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9+#.\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()