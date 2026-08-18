from tkinter.filedialog import askopenfilename
from pypdf import PdfReader
filename = askopenfilename()

reader= PdfReader(filename)
for cont in reader.pages:
    print(cont.extract_text())
