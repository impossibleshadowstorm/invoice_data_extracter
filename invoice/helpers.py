import os
import re
import pytesseract
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdf2image import convert_from_path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


PARSER = "parser"
KEYWORDS = "keywords"
FIELDS = "fields"
REGEX = "regex"
CWD = os.getcwd()

"""
    Data Extraction From PDF Using Miner
"""
def extraction_using_miner(path):
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue().lower()


"""
    Data Extraction From PDF but
    After Converting all pages to images and
    After that extracting the data out
"""
def extraction_using_tesseract(path):
    pages = convert_from_path(path, 500)
    data = ""
    for idx, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        data += text
    return data


"""
    Return the group of matched data from given text
"""
def find_with_regex(text, regex):
    Regex = re.compile(regex)
    m = Regex.search(text)
    return m.group()


def get_state_code_from_gstin(gstin):
    return gstin[:2]


def get_data(path_to_file):
    roughly_extracted_data = ""
    if path_to_file.lower().endswith(".pdf"):
        output = " ".join(extraction_using_miner(path_to_file).split())
        if(len(output) == 0):
            roughly_extracted_data = extraction_using_tesseract(path_to_file)
        else:
            roughly_extracted_data = extraction_using_miner(path_to_file)
    return roughly_extracted_data
