from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()
pdf.add_page('L')
pdf.add_page()

pdf.output('exemplo.pdf', 'F')
