from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

class ConversionPDF():
    """将 PDF 转换为其他文件格式"""
    def __init__(self, *filename):
        self.debug = 0
        self.password = b''
        self.pagenos = set()
        self.maxpages = 0
        self.outfile = None
        self.outtype = None
        self.imagewriter = None
        self.rotation = 0
        self.stripcontrol = False
        self.layoutmode = 'normal'
        self.encoding = 'utf-8'
        self.pageno = 1
        self.scale = 1
        self.caching = True
        self.showpageno = True
        self.laparams = LAParams()
        self.filename = filename
        