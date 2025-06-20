from .base_parser import BaseParser
import pymupdf

class PdfParser(BaseParser):
    def __init__(self):
        super().__init__()
        # self.file_path = file_path

    def parse(self, pdf_file_path):
        doc = pymupdf.open(pdf_file_path)
        content = ""
        for page in doc.pages():
            content += page.get_text()
        return content


if __name__ == '__main__':
    parser = PdfParser()
    print(parser.parse("../test_resources/kimi_vl.pdf"))
