from fpdf import FPDF

from .styles import *
from .detailsOrder import *

class structurePdf(FPDF):

    def header(self):
        #self.image('logo.png',
         #       x = 10, y = 10, w = 30, h = 30)

        self.set_font('Arial', '', 13)

        tcol_set(self, 'blue')
        tfont_size(self,45)
        tfont(self,'B')
        self.cell(w = 0, h = 20, txt = 'KLASS MUEBLES', border = 0, ln=1,
                align = 'C', fill = 0)

        tfont_size(self,10)
        tcol_set(self, 'black')
        tfont(self,'I')
        self.cell(w = 0, h = 10, txt = 'ÁREA DE PLANIFICACIÓN Y OPERACIONES', border = 0, ln=2,
                align = 'C', fill = 0)

        self.ln(5)

          # Information Order
        bcol_set(self, 'white')
        tfont_size(self,9)
        tfont(self,'B')
        # detailOrder(self, tuplaArrayCases, tuplaInformationHead)



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

