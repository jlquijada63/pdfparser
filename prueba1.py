
from PyPDF2 import PdfFileReader


reader = PdfFileReader("prueba.pdf")

result = reader.getDocumentInfo()

print(f"Title: {result.title}")
print(f"Author: {result.author}")
print(f"Creator: {result.creator}")
