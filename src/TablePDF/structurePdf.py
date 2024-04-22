from fpdf import FPDF

from .styles import *

class structurePdf(FPDF):

    def header(self):
        #self.image('logo.png',
         #       x = 10, y = 10, w = 30, h = 30)

        self.set_font('Arial', '', 15)

        tcol_set(self, 'blue')
        tfont_size(self,45)
        tfont(self,'B')
        self.cell(w = 0, h = 20, txt = 'NOVAPAN', border = 0, ln=1,
                align = 'C', fill = 0)

        tfont_size(self,10)
        tcol_set(self, 'black')
        tfont(self,'I')
        self.cell(w = 0, h = 10, txt = 'Generado el 2024/04/17', border = 0, ln=2,
                align = 'C', fill = 0)

        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt = str(self.page_no()) + '/{nb}',
                 border = 0,
                align = 'C', fill = 0)   

