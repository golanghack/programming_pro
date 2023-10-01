#! /usr/bin/env python3

from PyPDF2 import PdfFileMerger 

def by_appending_end() -> None:
    """Append another pdf file to one pdf file."""
    
    merger = PdfFileMerger()
    # stream
    file_one = open('samplePdf1.pdf', 'rb')
    merger.append(file_one)
    
    # direct file path 
    merger.append('samplePdf2.pdf')
    merger.write('mergerPdf.pdf')
    
def by_inserting() -> None:
    merger = PdfFileMerger()
    merger.append('samplePdf1.pdf')
    merger.merge(0, 'samplePdf2.pdf')
    merger.write('mergedPdf1.pdf')
    
if __name__ == '__main__':
    by_appending_end()
    by_inserting()