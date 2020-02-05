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
    help = """
    创建一个 ConversionPDF 对象以将 PDF 转换为 txt, tag, html 。 
    """

    def __init__(self):
        """初始化类"""
        self.v_debug = 0
        self.v_password = b''
        self.v_pagenos = set()
        self.v_maxpages = 0
        self.v_outfile = None
        self.v_outtype = None
        self.v_imagewriter = None
        self.v_rotation = 0
        self.v_stripcontrol = False
        self.v_layoutmode = 'normal'
        self.v_encoding = 'utf-8'
        self.v_pageno = 1
        self.v_scale = 1
        self.v_caching = True
        self.v_showpageno = True
        self.v_laparams = LAParams()
        self.v_filename = None
        
