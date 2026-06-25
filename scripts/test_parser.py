from app.services.pdf_parser import PDFParser

pdf_path = "D:/AI-Career-Intelligence/backend/uploads/bd3b67ba-e427-43cf-95b6-23337e37c58f.pdf"

text = PDFParser.extract_text(pdf_path)

print(text)