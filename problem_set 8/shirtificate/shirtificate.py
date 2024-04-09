from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("shirtificate.png", 0, 50, 210)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 20)
        # Moving cursor to the right:
        #self.cell(800)
        # Printing title:
        self.cell(0, 30, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)



# Instantiation of inherited class
gem = input('Name: ')
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png",x=None , y=80 , w=190 )
pdf.set_font("Times", size=20)
pdf.set_text_color(r=2,g=4,b=200)
pdf.cell(0, 200, f"{gem} took CS50 " , align='C' , )
pdf.output("shirtificate.pdf")