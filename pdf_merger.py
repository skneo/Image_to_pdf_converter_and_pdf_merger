#merging pdf
try:
    from PyPDF2 import PdfFileMerger
except:
    input('PyPDF2 library will be installed on your machine, press enter to continue\n')
    from pip._internal import main as pipmain
    pipmain(['install', 'PyPDF2'])
    try:
        from PyPDF2 import PdfFileMerger
    except:
        input("\nPyPDF2 library not installed. May be there is no internet connection, try again with active connection or manually install by running 'pip install PyPDF2' command in Command Prompt.\nPress enter to exit and run script again.")
        quit()
import os
pdfs = os.listdir('pdf_files')
merger = PdfFileMerger()
for pdf in pdfs:
    if(pdf.split(".")[1]=='txt'):
        continue
    merger.append('pdf_files/'+pdf)
merger.write('merged_pdfs.pdf')
merger.close()
input('***\nAll pdf files merged in merged_pdfs.pdf, press enter to close program\n***')
