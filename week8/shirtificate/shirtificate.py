from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', 'B', 30)

pdf.cell(210, 10, 'CS50 Shirtificate', 0, 1, 'C')

pdf.image('shirtificate.png', x=50, y=50, w=100, h=100)

pdf.set_font('Arial', '', 20)

name = input('Name: ')
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, name, 0, 1, 'C', True)

pdf.output('shirtificate.pdf', 'F')
